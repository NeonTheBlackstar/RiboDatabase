from BCBio import GFF
import sys

def getSeq(h_fasta):
	sq = ''
	for line in h_fasta:
		if line.startswith('>') == False:
			sq += line.strip()
	return sq
	
def translate(seq):
	dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	new_seq = ''
	for id in range(len(seq)):
		new_seq += dic[seq[id]]
	return new_seq

def printSeq(seq, x, y, strand, beforeStart, afterStart): # Zabezpieczyc przed wyjechaniem poza sekwencje!
	shdl = ''
	if strand == '+':
	# In + strand start codon is at x
		if x-beforeStart < 0:
			shdl += seq[0:x+afterStart]

			#print("1[{}, {}]".format(0, x+afterStart))
		elif x+afterStart >= len(seq):
			shdl += seq[x-beforeStart:len(seq) - 1]

			#print("2[{}, {}]".format(x-beforeStart, len(seq) - 1))
		else:
			shdl += seq[x-beforeStart:x+afterStart]	

			#print("3[{}, {}]".format(x-beforeStart,x+afterStart))	
	if strand == '-':
	# In - strand start codon is at y
		if y-afterStart < 0:
			shdl += seq[0:y+beforeStart]

			#print("1[{}, {}]".format(0, y+beforeStart))
		elif y+beforeStart >= len(seq):
			shdl += seq[y-afterStart:len(seq) - 1]

			#print("2[{}, {}]".format(y-afterStart, len(seq) - 1))
		else:
			shdl += seq[y-afterStart:y+beforeStart]

			#print("3[{}, {}]".format(y-afterStart,y+beforeStart))

		shdl = translate(shdl)
		shdl = shdl[::-1]

	shdl += '\t'+str(x)+'\t'+str(y)+'\t'+strand
	return shdl

def printToFasta(handle, seq, x, y, strand, id, additional, exhead):
	if(additional != ''):
		additional = '|' + additional

	if exhead == True:
		handle.write('>'+id+'|'+str(x)+'|'+str(y)+'|'+strand+additional+'\n')
	else:
		handle.write('>'+id+additional+'\n')
		
	handle.write(seq.split('\t')[0]+'\n')

def getParamValue(param, param_list):
	for i in range(0,len(param_list)):
		if param_list[i] == param and param.startswith('-'):
			if i + 1 < len(param_list):
				return param_list[i+1]
			else:
				print("No value for parameter was given")
				break
	return None

'''
Arguments:
1. -gff = GFF file
2. -fasta = Genom sequence in Fasta
3. -before = Nucleotides before Start
4. -after = Nucleotides after Start
5. -meme = Meme output file to extract subsequence basing on motifs' positions
6. -filter = Filter
7. -exhead = Print extended fasta header including position and strand info
8. -aptamer = Exclusive parameter for extracting subseqs for aptamer finding. Value is how many nucleotides after preceding gene START to take as a left interval boundary, if preceding gene STAR postion starts before earlier than -500 nucs from STAR of our gene
'''
def getFasta(*arg):
	gene_filter = getParamValue('-filter',arg)				# ValueType: Dictionary { key: list(2) }
	beforeStart = getParamValue('-before',arg)				# ValueType: Integer
	afterStart = getParamValue('-after',arg)				# ValueType: Integer
	gff_path = getParamValue('-gff',arg)					# ValueType: String
	fasta_path = getParamValue('-fasta',arg)				# ValueType: String
	meme_path = getParamValue('-meme',arg)					# ValueType: String
	exhead = getParamValue('-exhead',arg)					# ValueType: Boolean
	aptamerInterval = getParamValue('-aptamer',arg)			# ValueType: Integer
	meme = None
	handle = None
	h_fasta = None
	previous_gene = None

	### CHECK CONDITIONS ###

	if gff_path != None:
		handle = open(gff_path)
	if fasta_path != None:
		h_fasta = open(fasta_path)
	if meme_path != None:
		meme = open(meme_path, "r")
		fileName = 'rnafold_seqs'
	else:
		fileName = 'ribsw_pos_window'

	out_fasta = open(fileName + '.fasta', 'w')
	sequence = getSeq(h_fasta)
	h_fasta.close()
	counter = 0

	for record in GFF.parse(handle):
		for feature in record.features:
			if feature.type == 'gene':
				### Reset modified values ###
				beforeStart = getParamValue('-before',arg)
				afterStart = getParamValue('-after',arg)

				# Start and end values are related to GFF notation, it does not represent the real direction of a strand.
				start = feature.location.start # Automatically substract 1, so it matches ID array notation
				end = feature.location.end
				seqSymbol = '+' if feature.strand == 1 else '-'

				preBefore = beforeStart

				if previous_gene != None:
					previous_strand = '+' if previous_gene.strand == 1 else '-'
					previous_start = previous_gene.location.start
					previous_end = previous_gene.location.end

					if seqSymbol == previous_strand:
						if seqSymbol == '+':
							if previous_start + aptamerInterval > start - beforeStart: # Cos jest zle???
								beforeStart = start - previous_start + aptamerInterval

						if seqSymbol == '-':
							if previous_end - aptamerInterval < end + beforeStart:
								beforeStart = previous_end - aptamerInterval - end

				#if seqSymbol == '+' and beforeStart > 500:
				#	print("previous {} now {}".format(preBefore,beforeStart))

				if gene_filter != None:
					filterFound = False
					for key in sorted(gene_filter):
						if key == feature.qualifiers['locus_tag'][0]:
							# GET POSITIONS HERE #
							if(start > gene_filter[key][0]):
								beforeStart = start - gene_filter[key][0]
							else:
								beforeStart = gene_filter[key][1] - end
							afterStart = 20
							
							filterFound = True
							break
					if filterFound == False: # If not found in filter, then don't add it to output file
						continue
				if meme != None: #for current record if it's in meme output file, if yes, then pass it to the output fasta
					meme.seek(0,0)
					found = False
					for line in meme:
						name = line.split('\t')[0]
						name = name.split('|')[1]

						if name == feature.qualifiers['locus_tag'][0]:
							found = True
							break 
					if found == False:
						continue

				window = printSeq(sequence, start, end, seqSymbol, beforeStart, afterStart)
				printToFasta(out_fasta, window, start, end, seqSymbol, feature.qualifiers['locus_tag'][0], '', exhead)
				counter += 1

				### PREVIOUS GENE ###
				if aptamerInterval != None:
					previous_gene = feature
	handle.close()
	out_fasta.close()
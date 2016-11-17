from BCBio import GFF
import sys
import re
from suboptimals import is_number

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

def printSeq(seq, x, y, strand, beforeStart, afterStart):
	shdl = ''
	if strand == '+':
	# In + strand start codon is at x
		shdl += seq[x-beforeStart:x+afterStart]
		#print(shdl)
	if strand == '-':
	# In - strand start codon is at y
		shdl += seq[y-afterStart:y+beforeStart]
		#print('not translated: '+shdl)
		shdl = translate(shdl)
		#print('translated: '+shdl)
		shdl = shdl[::-1]
		#print('reversed: '+shdl)
	shdl += '\t'+str(x)+'\t'+str(y)+'\t'+strand
	return shdl

def printToFasta(handle, seq, x, y, strand, id, additional, len_arg):
	if(additional != ''):
		additional = '|' + additional

	if(len_arg >= 5):
		handle.write('>'+'b_sub|'+id+'|'+str(x)+'|'+str(y)+'|'+strand+additional+'\n')
	else:
		handle.write('>'+'b_sub|'+id+additional+'\n')
		
	handle.write(seq.split('\t')[0]+'\n')

'''
Arguments:
1. GFF file
2. Genom sequence in Fasta
3. Nucleotides before Start
4. Nucleotides after Start
5. Meme output file to extract subsequence basing on motifs' positions
'''
def getFasta(*arg):
	doFilter = False
	fromAptamers = False
	gene_filter = {}

	beforeStart = int(arg[2]) #sys.argv[3]
	if len(arg) >= 4 and is_number(str(arg[3])):
		afterStart = int(arg[3]) #sys.argv[4]
	else:
		afterStart = 0

	handle = open(arg[0], "r") # GFF file | sys.argv[0]
	h_fasta = open(arg[1], "r") # Inout fasta genome | file sys.argv[1]
	if len(arg) >= 5:
		meme = open(arg[4], "r") # Meme output file if given | sys.argv[4]
		fileName = 'rnafold_seqs'
	else:
		meme = ''
		fileName = 'shi-dal_output'
	
	if len(arg) >= 6 or len(arg) >= 4:
		if not is_number(str(arg[3])):
			gene_filter = arg[3]
		else:
			gene_filter = arg[5]
			fromAptamers = True
		doFilter = True

	out_fasta = open(fileName + '.fasta', 'w')
	sequence = getSeq(h_fasta)
	h_fasta.close()
	counter = 0

	for record in GFF.parse(handle): # We have only one record in the file, so the loop is uneccessary
		for feature in record.features:
			if feature.type == 'gene':
				start = int(str(feature.location)[1:].split(':')[0]) # Get codon start position (in +)
				end = int(str(feature.location)[1:].split(':')[1].split(']')[0])
				seqSymbol = str(feature.location).split('(')[1][0] # Get strand symbol - or +
				
				if doFilter == True:
					#print(feature.qualifiers['locus_tag'])
					filterFound = False
					for key in sorted(gene_filter):
						#print('Key: '+key+', l_t: '+feature.qualifiers['locus_tag'][0])
						if key == feature.qualifiers['locus_tag'][0]:
							# GET POSITIONS HERE #
							#print(feature.id + ', strand: ' + seqSymbol)
							if fromAptamers:
								if(start > gene_filter[key][0]):
									beforeStart = start - gene_filter[key][0]
									#print(start - gene_filter[key][0])
								else:
									beforeStart = gene_filter[key][1] - end
									#print(gene_filter[key][1] - end)
								afterStart = 20
							
							filterFound = True
							break
							#print(feature.id)
					if filterFound == False:
						continue
				if meme != '': # Look for current record if it's in meme output file, if yes, then pass it to the output fasta
					meme.seek(0,0)
					found = False
					for line in meme:
						name = line.split('\t')[0]

						name = name.split('|')[1]
						if name == str(feature.qualifiers['ID'])[2:-2]:
							found = True
							break 
					if found == False:
						continue
				window = printSeq(sequence, start, end, seqSymbol, beforeStart, afterStart)
				printToFasta(out_fasta, window, start, end, seqSymbol, str(feature.qualifiers['ID'])[2:-2], '', len(arg))
				counter += 1			
	handle.close()
	out_fasta.close()	

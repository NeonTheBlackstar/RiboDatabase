import sys
from BCBio import GFF

def printToBed(structure_out, _gene, gff_path, score, start, end, strand):
	counter = 0
	handle = open(gff_path, 'r')
	for record in GFF.parse(handle): # We have only one record in the file, so the loop is uneccessary
		for feature in record.features:
			if feature.type == 'gene' and feature.id == _gene:
				#start = int(str(feature.location)[1:].split(':')[0]) # Get codon start position (in +)
				#end = int(str(feature.location)[1:].split(':')[1].split(']')[0])
				locus_tag = feature.qualifiers['locus_tag'][0]				

				structure_out.write('{}\t{}\t{}\t{};{}\t{}\t{}\n'.format(record.id,start,end,_gene, locus_tag, strand, score))
	handle.close()
	
# bound_param: parametr określający ile nukleotydów musi być niezwiązanych. procentowy od 0.0 do 1.0.
def findSwitch(bound_param, gff_path, record_name):
	structure_out = open('./Results/' + record_name + '.shine.bed','w')
	meme = open('./Programs/shine-dalgarno/meme_output.txt','r')
	barrier_output = open('suboptimals.fasta','r')
	
	pos_from = 0
	pos_to = 0
	_from = 0
	_to = 0
	_sd_pos_start = 0 # Shine dalgarno absolute position (in .fasta)
	_sd_pos_end = 0
	is_switch = False				
	fasta_id = ''
	_gene = ''
	for line in barrier_output:
		if line[0] == '>':
			pos_from = 0
			pos_to = 0
			is_switch = False
					
			fasta_id = line
			id_list = line.split('|')
			_gene = id_list[1]
			_gene_start = int(id_list[2])
			_gene_end = int(id_list[3])
			_strand = id_list[4].rstrip()
			
			for line in meme:
				free = True

				_list = line.split('\t')
				_desc = _list[0].split('|')
				gene_id = (_desc[1])
				
				if gene_id == _gene:
					_from = int(_desc[2])
					_to = int(_desc[3])
					#print('|'+_strand.rstrip()+'|'+str(_gene_start)+';'+str(_gene_end))
					if _strand == '+':
						_sd_pos_start = _gene_start - _from
						_sd_pos_end = _gene_start - _to
					elif _strand == '-':
						_sd_pos_start = _gene_end + _to # meme pos format e.g. 17|9
						_sd_pos_end = _gene_end + _from
					printToBed(structure_out, _gene, gff_path, 0, _sd_pos_start, _sd_pos_end, _strand)
					break
			meme.seek(0)
		else:
			if _from != 0 and _to != 0:
				structure = line.strip()
			
				codon = len(structure) - 20 # Position of codon based on window parameters
				pos_from = codon - _from
				pos_to = codon - _to
			
				sd_length = pos_to - pos_from
				points = 0
				for id in range(pos_from, pos_to):
					if structure[id] == '.':
						points += 1		
				score = points/sd_length
				if score >= bound_param:
					pass
					#printToBed(structure_out, _gene, gff_path, score)
	structure_out.close()
	barrier_output.close()

#findSwitch(0.5, '../../Genomes/bacillus.gff', 'NC_000964.3')

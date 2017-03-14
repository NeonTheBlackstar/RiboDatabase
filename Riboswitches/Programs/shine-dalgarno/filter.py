
import random
from BCBio import GFF

# Creates gene filter for .gff file basing on aptamer records in .ptt file and terminator records in .bed.
# Script adds aptamers records to matrix and removes terminator records (as there is no transaltion termination by bindig shine-dalgarno)
def createGffFilter(ptt_file, bed_file):
	filter_matrix = {}
	ptt_handle = open(ptt_file, 'r')
	
	with open(ptt_file) as ptt_handle:
		count = 0
		for line in ptt_handle:
			count+=1
			if count % 2 == 0 and count >= 4:
				line_list = line.split('\t')
				gene_id = line_list[8].split(';')[1].rstrip()
				_from = line_list[0].split('..')[0]
				_to = line_list[0].split('..')[1]			
				filter_matrix[gene_id] = (int(_from), int(_to))			
	with open(bed_file) as bed_handle:
		for line in bed_handle:
			line_list = line.split('\t')
			gene_id = line_list[3].split(';')[2]
			if gene_id in filter_matrix:
				filter_matrix.pop(gene_id, None)
	return(filter_matrix)

def prepareSample(filter_matrix, gff_path):
	random.seed()
	candidate_list = []
	handle = open(gff_path, 'r')
	gene_count = 0
	for record in GFF.parse(handle):
		for feature in record.features:
			if feature.type == 'gene':
				locus_tag = feature.qualifiers['locus_tag'][0]
				isMatch = False
				gene_count += 1
				for key in filter_matrix:
					if key == locus_tag:
						isMatch = True
						break
				if isMatch == False:
					candidate_list.append(locus_tag)
	countToAdd = round(gene_count / 2) - len(filter_matrix)
	if countToAdd > 0:
		for i in range(1, countToAdd):
			list_len = len(candidate_list)
			list_id = random.randint(0, list_len - 1)
			locus_str = candidate_list[ list_id ]
			filter_matrix[locus_str] = (0, 0)
			candidate_list.remove( locus_str )
				
	handle.close()
	return(filter_matrix)
            			
#createGffFilter('NC_000964.3.ptt','NC_000964.3.terminators.bed')
		

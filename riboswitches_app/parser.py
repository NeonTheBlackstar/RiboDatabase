import csv

'''
This script reads csv file and divides it to lists. Every row in csv file is a single list. 
Script uses lists in list construction.
First list contains names of columns in csv file. Proper data starts from the secon list (first index).

Lack of the values in csv file is displayed as an empty quotes.

Column names: ligand [0], class [1], name [2], organism [3], gene [4], operon [5], mechanism [6], effect [7], confirmation of mechanism [8],
position in genome [9], sequence [10], secondary structure [11], 3D structure [12], other references [13] (indexed from one :, so e.g. l[1][5], l[2][0] etc.).

Examples:
l[2][1] is a class name of second switch in csv file
l[4][7] is an effect which has eight switch in csv file

'''


def loadDataToDictionary(fileName):
	'''
	Dictionary that represents all possible data which can be obtained for a single riboswitch record:
	'''
	d = {
			# Record #
		'switch_name': '',
		'switch_sequence': '',
		'operon_genes': '',
		'3d_structure': '',
		'effect': '',
		'mechanism': '',
		'strand': '0',
		'switch_start': 0,
		'switch_end': 0,
			# RiboClass #
		'rcl_name': '',
		'rcl_description': '',
		'rcl_alignment': '',
			# RiboFamily #
		'rfam_name': '',
		'rfam_description': '',
		'rfam_alignment': '',
			# Gene #
		'gene_name': '',
		'gene_accession_number': '',
		'gene_start': 0,
		'gene_end': 0,
		'taxonomy_id': 0,
			# Organism #
		'scientific_name': '',
		'common_name': '',
		'or_accession_number': '',
			# LigandClass #:
		'lic_name': '',
		'lic_description': '',
			# Ligand #
		'li_name': '',
		'li_description': '',
			# Structure 2D #
		'without_ligand': '',
		'with_ligand': '',
		'predicted': '',
			# Terminator #
		'tr_start': 0,
		'tr_end': 0,
			# Promoter #
		'pr_start': 0,
		'pr_end': 0,
			# Articles #
		'articles': '',
	}

	extension = fileName.split('.')[1]
	if extension == 'csv':
		return csvParser(d, fileName)

def csvParser(d, fileName):
	dList = [] # List of row data dictionaries
	spamReader = csv.reader(open(fileName, newline = ''), delimiter = '\t') # Construction for Python3
		data = [list(row) for row in spamReader]
		labels = data[0]
		for row in data[1:]:
			dic = d.copy()
			for id in range(0, len(labels)):
				label_name = labels[id].lower().strip() # Lowercase all letters to prevent case sensitivity
				elem_data = row[id]
				if label_name in d:
					dic[label_name] = elem_data.strip()
				elif label_name.replace(' ', '_') in d: # Underscores in label names can be replaced with spaces for readability
					dic[label_name.replace(' ', '_')] = elem_data.strip()
			dList.append(dic)
	return(dList)
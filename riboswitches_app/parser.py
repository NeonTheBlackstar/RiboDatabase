import csv
from re import match
import xml.etree.ElementTree as ET

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

def readAttrb(value, default = None):
	default = value if default == None else default

	if (isinstance(default, int) and isinstance(value, str)) or value == '':
		return(default)
	elif isinstance(default, str) and isinstance(value, str):
		return(value.strip())
	elif isinstance(default, int) and isinstance(value, int):
		return(int(value))


def loadDataToDictionary(fileName):
	'''
	Dictionary that represents all possible data which can be obtained for a single riboswitch record:
	'''
	d = {
			# Record #
		'switch_name': '',
		'switch_sequence': '',
		'operon_genes': '',
		'structure_3d': '',
		'effect': '.',
		'mechanism': 'UN',
		'strand': '.',
		'switch_start': 0,
		'switch_end': 0,
			# RiboClass #
		'class_name': '',
		'class_description': '',
		'class_alignment': '',
			# RiboFamily #
		'family_name': '',
		'family_description': '',
		'family_alignment': '',
			# Gene #
		'gene_name': '',
		'gene_accession_number': '',
		'gene_start': 0,
		'gene_end': 0,
			# Organism #
		'scientific_name': '',
		'common_name': '',
		'organism_accession_number': '',
		'taxonomy_id': 0,
			# LigandClass #:
		'ligand_class_name': '',
		'ligand_class_description': '',
			# Ligand #
		'ligand_name': '',
		'ligand_description': '',
			# Structure 2D #
		'without_ligand': '',
		'with_ligand': '',
		'predicted': '',
			# Terminator #
		'terminator_start': 0,
		'terminator_end': 0,
			# Promoter # 
		'promoter_start': 0,
		'promoter_end': 0,
			# Articles #
		'articles': '',
	}

	extension = fileName.split('.')[1]
	if extension == 'csv':
		return csvParser(d, fileName)
	elif extension == 'xml':
		return xmlParser(d, fileName)

def csvParser(d, fileName):
	dList = [] # List of row data dictionaries
	spamReader = []
	file = open(fileName, newline = '')
	# Determine a type of delimiter #
	first_line = file.readline()
	semicolon = match("[a-zA-Z0-9_ ]+;", first_line)
	tab = match("[a-zA-Z0-9_ ]+\t", first_line)
	file.seek(0)

	if tab != None:
		spamReader = csv.reader(file, delimiter = '\t')
	elif semicolon != None:
		spamReader = csv.reader(file, delimiter = ';')

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


def readSwitchFromXML(dic, root, parent):

	for elem_key in root.attrib:
		alternative_name = "{}_{}_{}".format(parent.tag, root.tag, elem_key)
		alternative_name2 = "{}_{}".format(root.tag, elem_key)

		if elem_key in dic:
			dic[elem_key] = readAttrb( root.attrib[elem_key] , dic[elem_key])
		elif alternative_name in dic:
			dic[alternative_name] = readAttrb( root.attrib[elem_key] , dic[alternative_name])
		elif alternative_name2 in dic:
			dic[alternative_name2] = readAttrb( root.attrib[elem_key] , dic[alternative_name2])

	for elem in root:
		readSwitchFromXML(dic, elem, root)

	return(dic)

def xmlParser(d, fileName):
	tree = ET.parse(fileName)
	root = tree.getroot()
	dList = []

	for switch in root:
		dic = d.copy()
		dList.append( readSwitchFromXML(dic, switch, root) )
		
	return(dList)
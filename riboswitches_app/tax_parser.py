import sys

organisms_list = []
l = [] #main list
#562 1423

def search_taxID(tax_id):

	fh_nodes = open('nodes.dmp', 'r')
	fh_names = open('names.dmp', 'r')
	
	name = ''

	for i in fh_nodes:
		nodes_id = int(i.split('|')[0].strip()) # id from nodes.dmp

		if tax_id == 1: # stop condition
			organisms_list.append(l.copy())
			return l

		if tax_id == nodes_id:
			for j in fh_names:
				tax_level = i.split('|')[2].strip() # species, genus etc.
				names_id = int(j.split('|')[0].strip()) # id from names.dmp
				data_type = j.split('|')[3].strip() # scientific_name, synonym, authority etc.

				if names_id == nodes_id and data_type == 'scientific name':
					name = j.split('|')[1].strip()

			l.append([nodes_id, name, tax_level])
			print(l)
			tax_id = int(i.split('|')[1].strip()) # new tax id which is parent id
			search_taxID(tax_id)
			return l

	fh_nodes.close()
	fh_names.close()

def create_load_file():

	tax_names = []
	tax_ids = []

	with open('taxonomy', 'w+') as out_file:
		out_file.write('{0}	{1}	{2}\n'.format('scientific_name', 'taxonomy_name', 'taxonomy_id'))
		
		for single_organism in organisms_list:
			for tax_list in single_organism:
				tax_names.append(tax_list[1])
				tax_ids.append(str(tax_list[0]))

				if tax_list[2] == 'species': # write name of the organism
					out_file.write('{0}	'.format(tax_list[1]))

			out_file.write('{0}	{1}\n'.format(','.join(tax_names), ','.join(tax_ids)))
			tax_names = []
			tax_ids = []

for i in sys.argv[1:]:
	search_taxID(int(i))
	l = []

create_load_file()

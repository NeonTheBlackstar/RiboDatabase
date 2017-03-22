import sys

#nodes - tax_id | parent tax_id
#names - tax_id | name
d = {}
l = []

fh_nodes = open('nodes.dmp', 'r')
for i in fh_nodes:
	d[i.split()[0]] = i.split()[2] # d[tax_id]: parent tax_id
fh_nodes.close()

def search_taxID(tax_id):

	for key, value in d.items():
		if tax_id == 1:
			return l
		
		if int(key) == tax_id:
			l.append(int(value))
			print(value)
			tax_id = l[-1]
			search_taxID(int(tax_id))
			return l


search_taxID(int(sys.argv[1]))
d = {}
d[sys.argv[1]] = l
print(d)

#from database.models import RiboFamily, RiboClass
from database.models import *
from parser import csvParser
from os import system

'''
# To delete all data in all tables without removing tables themselves:
	python3 manage.py flush
# To delete single model data use:
	ModelName.objects.all().delete()
'''

system('python3 manage.py flush --noinput')

csv_data = csvParser('switche2.csv')

for row in csv_data[1:]:
	v_riboclass = RiboClass.objects.create(name = row[1])
	v_ribofamily = RiboFamily.objects.create(ribo_class = v_riboclass, name = row[1])
	v_organism = Organism.objects.create(common_name = row[3], scientific_name = row[3])
	v_gene = Gene.objects.create(organism = v_organism, name = row[4])
	'''
	v_structure = Structure.objects.create(predicted = row[11])
	v_ligand = Ligand.objects.create(name = row[0])
	v_article = Article.objects.create(pmid = int(row[8]))

	_mechanism = 'UN'
	if row[6] == 'translation':
		_mechanism = 'TRL'
	elif row[6] == 'transcription':
		_mechanism = 'TRN':
	elif row[6] == 'degradation':
		_mechanism = 'DG'
 	
	v_record = Record.objects.create(
		family = v_ribofamily,
		gene = v_gene,
		structure = v_structure,
		organism = v_organism,
		ligand = v_ligand,
		article = v_article,
		name = row[2],
		sequence = row[10],
		start_pos = int(row[9]),
		end_pos = int(row[9]) + len(int(row[10])) if row[9] != '' and row[10] != '' else 0, # Ribo end position is start position add length of sequence IF both are given
		genes_under_operon_regulation = row[5],
		_3D_structure = row[12],
		effect = row[7],
		mechanism = _mechanism
	)'''

'''
for i in RiboClass.objects.all():
	i.delete()

for i in RiboFamily.objects.all():
	i.delete()


c = RiboClass(name = 'NazwaC', description = 'OpisC', alignment = 'AlajC')
c.save()
f = RiboFamily(ribo_class = c, name = 'NazwaF', description = 'OpisF', alignment = 'AlajF')
f.save()

c = RiboClass(name = 'NazwaC2', description = 'OpisC2', alignment = 'AlajC2')
c.save()
f = RiboFamily(ribo_class = c, name = 'NazwaF2', description = 'OpisF2', alignment = 'AlajF2')
f.save()



print(RiboFamily.objects.all())
print(RiboClass.objects.all())
c = RiboClass.objects.all()[0]
print(c.ribofamily_set.all())
'''

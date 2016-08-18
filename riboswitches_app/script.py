'''
# First argument is filename for csv parser
	python3 script.py switche2.csv
# To delete all data in all tables without removing tables themselves using manage.py:
	python3 manage.py flush --noinput
# To delete single model data:
	ModelName.objects.all().delete()
# To import only a few models:
	from database.models import RiboFamily, RiboClass
'''

from parser import csvParser
import os
from sys import argv

''' This tells Django where to look for our project's settings '''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riboswitches_app.settings")
''' This allows to load our models' file '''
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
''' Finally import out models '''
from database.models import *
''' To use managing functions inside script: '''
from django.core.management import execute_from_command_line
execute_from_command_line([argv[0], 'flush', '--noinput']) # Function argument is like sys.argv - a list

csv_data = csvParser(argv[1])
#row = csv_data[1]
#v_riboclass = RiboClass.objects.create(name = row[1])

#print(csv_data)
#print(RiboClass.objects.all())


for row in csv_data[1:]:
	row = [None if element == '' else element for element in row]
	print(row)
	v_riboclass = RiboClass.objects.create(name = row[1])
	'''
	v_ribofamily = RiboFamily.objects.create(ribo_class = v_riboclass, name = row[1])
	
	
	v_organism = Organism.objects.create(common_name = row[3], scientific_name = row[3])
	v_gene = Gene.objects.create(organism = v_organism, name = row[4])
	
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

glycine	B	glycine	Bacillus subtilis	gcvT	gcvPA, gcvPB	transcription	+	15472076		AUAUGAGCGAAUGACAGCAAGGGGAGAGACCUGACCGAAAACCUCGGGAUACAGGCGCCGAAGGAGCAAACUGCGGAGUGAAUCUCUCAGGCAAAAGAACUCUUGCUCGACGCAACUCUGGAGAGUGUUUGUGCGGAUGCGCAAACCACCAAAGGGGACGUCUUUGCGUAUGCAAAGUAAACUUUCAGGUGCCAGGACAGAGAACCUUCAUUUUACAUGAGGUGUUUCUCUGUCCUUUUUU	……………((((((((……((((.((((…..))))….)))).(((…((((…(((….)))….))))..)))…….))))))))……..(((((……((((((((….)))))))).(((…((((…(.(((((….))))))….))))..)))…….)))))…((((((…..))))))……………….		23249744, 23721735
glycine	C	glycine	SAR11 - Cand. P. ubique (Pelagibacter ubique)	glcB		transcription	+	19125817		UAAUUGAUAUCGGGAGAGACCAUUAAUAAUAGCGCCGAAGGAGCAACCACCCCGGAAACUCUCAGGCAAAUGGACCGAUAACAACAAUAACACUCUGGAAAGAGAUUUAUCUCGCCGAUGGAGCAAAACUCUCAGGCAAAAAUACAGAUGGGGUAAA	……..(((((……((((…..)))).(((…((((…((…..))…))))..)))…….)))))…………..((((….((((….))))(((…((((…..))))..)))…….))))………		
glycine	D	glycine	Granulibacter bethesdensis CGDNIH1	glcB		transcription	+	homology					19125817
glycine	E	glycine	Streptomyces griseus	gcvP		transcription	+	24443533		UGGCUGCUGACCCCGUGCGGGAGAGUCCUCCGGUCCAGAAUCCGGAGGCGCCGAAGGAGCAACUCCUCCCCGGAAUCUCUCAGGCCCCCGUACCGCACGGACGAGGUCACUCUGGAAAGCAGGGCGGUUCCGUGCGGGCGCAGGCCCGGGUGGAUUCGACCCUCACCGACGGUGAAAGCCGGCACGCCCCCGGGCGGGCCGGUGAAGCUCUCAGGUUGAGAUGACAGAGGGG	…………((((((((……(((((((……..))))))).(((…((((….(((…..)))..))))..)))…….))))))))………(((((……(((((((.(((((.(((((….))))).))))).))).)))).(.(…((.(….(((((.((((….)))).)))))…..).))…).)…….)))))…		
glycine	F	glycine	Streptomyces griseus	gcvT	gcvH	transcription	+	24443533		GAAUCCGCGCGGGAGAGUUCCGGCCACACUGUGAGCCGGGCGCCGAAGGAGCAAGAUCCUCCCUUGAAUCUCUCAGGCCCCGUACCGCGCGGAUGAGGCAGAUCUGAAAAGCGAGCCGUUCCACGGCUCCACCCAAGGUGCAAGCCGAGCCCCCUGAUCCGGGGCGCCCUCCAGGGGCAUACCCCGUCGGGGGCUAUCGGCGAACCUCUCAGGUUCCGAUGACAGAUGGGG	..(((((((.(((…..((((((……….)))))).(((..(((((…..((…….))..))))).)))……))))))))))…….(((((……(((((((…))))))).(.((..((.(……….((((((……………))))))……………………….).))..)).)…….)))))….		
glycine	G	glycine	Fusobacterium nucleatum			transcription	+	18042658	AE009951.2	GAUAUGAGGAGAGAUUUCAUUUUAAUGAAACACCGAAGAAGUAAAUCUUUCAGGUAAAAAGGACUCAUAUUGGACGAACCUCUGGAGAGCUUAUCUAAGAGAUAACACCGAAGGAGCAAAGCUAAUUUUAGCCUAAACUCUCAGGUAAAAGCACGGAG	((((((((……((((((((….)))))).(((…((((…..))))..)))……..))))))))……..(((((……(((((…..))))).(((…((((….((((….))))…..))))..)))…….)))))	3P49	21439473, 22192063, 23060425, 23249744, 24318897



'''

print(RiboClass.objects.all())
#print(RiboFamily.objects.all())

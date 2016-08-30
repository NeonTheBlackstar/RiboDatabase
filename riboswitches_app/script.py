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
from django.db import IntegrityError
from re import match

''' This tells Django where to look for our project's settings '''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riboswitches_app.settings")
''' This allows to load our models' file '''
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
''' Finally import out models '''
from database.models import *
''' To use managing functions inside script: '''
from django.core.management import execute_from_command_line
''' Removes whole data from database. Comment following line if it's not necessary '''
execute_from_command_line([argv[0], 'flush', '--noinput'])

# For text fields with NOT NULL integrity constraint (mostly primary keys) we replace empty strings with None value, so an exception (NOT NULL INTEGRITY ERROR) will be called and such object won't be added to database 
def emptyToNone(text):
	return None if text == '' else text

csv_data = csvParser(argv[1])

for row in csv_data[1:]:
	row = [element.strip() for element in row]
	
	''' CREATING NEW OBJECTS '''
	v_riboclass = None # Pointer for RiboClass object
	v_ribofamily = None
	v_organism = None
	v_gene = None
	v_structure = None
	v_ligand = None
	v_article = [] # List of pointers for Article objects

	''' RiboClass '''
	'''
	try:
		v_riboclass = RiboClass.objects.create(emptyToNone(name = row[1]))
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_riboclass = RiboClass.objects.get(name = row[1])
		elif match("NOT NULL", str(e)):
			v_riboclass = None
	'''

	''' RiboFamily '''
	try:
		v_ribofamily = RiboFamily.objects.create(ribo_class = v_riboclass, name = emptyToNone(row[1]))
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_ribofamily = RiboFamily.objects.get(name = row[1])
		elif match("NOT NULL", str(e)):
			v_ribofamily = None

	''' Organism '''
	try:
		v_organism = Organism.objects.create(scientific_name = emptyToNone(row[3]))
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_organism = Organism.objects.get(scientific_name = row[3])
		elif match("NOT NULL", str(e)):
			v_organism = None

	''' Gene '''
	try:
		v_gene = Gene.objects.create(organism = v_organism, name = emptyToNone(row[4]))
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_gene = Gene.objects.get(organism = v_organism, name = row[4])
		elif match("NOT NULL", str(e)):
			v_gene = None
	
	''' Structure '''
	try:
		v_structure = Structure.objects.create(predicted = row[11])
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_structure = Structure.objects.get(predicted = row[11])
		elif match("NOT NULL", str(e)):
			v_structure = None

	''' Ligand '''
	try:
		v_ligand = Ligand.objects.create(name = emptyToNone(row[0]))
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_ligand = Ligand.objects.get(name = row[0])
		elif match("NOT NULL", str(e)):
			v_ligand = None

	''' Article - ManyToMany relation '''
	article_ids = row[13].split(', ')
	temp_art = None

	for art in article_ids:
		try:
			if art != '': # NOT NULL exception is not threw in IntegerField, so I prevented adding wrong data this way
				temp_art = Article.objects.create(pmid = art)
				v_article.append(temp_art)
		except IntegrityError as e:
			if match("UNIQUE", str(e)):
				temp_art = Article.objects.get(pmid = art)
				v_article.append(temp_art)

	_mechanism = 'UN'
	if row[6] == 'translation':
		_mechanism = 'TRL'
	elif row[6] == 'transcription':
		_mechanism = 'TRN'
	elif row[6] == 'degradation':
		_mechanism = 'DG'

	_effect = 1 if row[7] == '+' else '-' if row[7] == '-' else 0
	
	v_record = Record.objects.create(
		family = v_ribofamily,
		gene = v_gene,
		structure = v_structure,
		organism = v_organism,
		ligand = v_ligand,
		name = row[2],
		sequence = row[10],
		#start_pos = 0, #int(row[9]),
		#end_pos = 0, #int(row[9]) + len(int(row[10])) if row[9] != '' and row[10] != '' else 0, # Ribo end position is start position add length of sequence IF both are given
		genes_under_operon_regulation = row[5],
		_3D_structure = row[12],
		effect = _effect,
		mechanism = _mechanism,
	)
	''' Add ManyToMany relations '''
	# Articles #
	for it in v_article:
		v_record.articles.add(it)

for e in Record.objects.all():
	print('\n\n')
	print(e)
	print('\n\n')

'''
for i in RiboClass.objects.all():
	i.delete()

c = RiboClass(name = 'NazwaC', description = 'OpisC', alignment = 'AlajC')
c.save()

print(RiboFamily.objects.all())
'''

#print(RiboClass.objects.all())
#print(RiboFamily.objects.all())

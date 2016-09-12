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

from parser import csvParser, loadDataToDictionary
import os
from sys import argv, exit
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
''' Removes whole data from database. Comment following line if it's not necessary ''' ###################################
execute_from_command_line([argv[0], 'flush', '--noinput'])

dList = loadDataToDictionary(argv[1])

for row in dList:
	''' CREATING NEW OBJECTS '''
	v_riboclass = None # Pointer for RiboClass object
	v_ribofamily = None
	v_organism = None
	v_gene = None
	v_structure = None
	v_ligandclass = None
	v_ligand = None
	v_article = [] # List of pointers for Article objects

	''' RiboClass '''
	try:
		if row['rcl_name'] != '':
			v_riboclass = RiboClass.objects.create(
				name = row['rcl_name'], # Primary Key
				description = row['rcl_description'],
				alignment = row['rcl_alignment'],
			)
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_riboclass = RiboClass.objects.get(name = row['rcl_name'])

	''' RiboFamily '''
	try:
		if row['rfam_name'] != '':
			v_ribofamily = RiboFamily.objects.create(
				ribo_class = v_riboclass,
				name = row['rfam_name'], # Primary Key
				description = row['rfam_description'],
				alignment = row['rfam_alignment'],
			)
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_ribofamily = RiboFamily.objects.get(name = row['rfam_name'])

	''' Organism '''
	try:
		if row['scientific_name'] != '':
			v_organism = Organism.objects.create(
				scientific_name = row['scientific_name'],
				common_name = row['common_name'],
				accession_number = row['or_accession_number'],
			)
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_organism = Organism.objects.get(scientific_name = row['scientific_name'])

	''' Gene '''
	try:
		if row['gene_name'] != '':
			v_gene = Gene.objects.create(
				organism = v_organism, 
				name = row['gene_name'],
				accession_number = row['gene_accession_number'],
				taxonomy_id = row['taxonomy_id'],
			)

			if row['gene_start'] != 0 or row['gene_end'] != 0:
				v_gene.position = Position.objects.create(start = row['gene_start'], end = row['gene_end'])
			else:
				v_gene.position = None
			v_gene.save()
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_gene = Gene.objects.get(organism = v_organism, name = row['gene_name'])
	
	''' Structure '''
	if row['without_ligand'] != '' or row['with_ligand'] != '' or row['predicted'] != '':
		v_structure = Structure.objects.create(
			predicted = row['predicted'],
			with_ligand = row['with_ligand'],
			without_ligand = row['without_ligand'],
		)

	''' LigandClass '''
	try:
		if row['lic_name'] != '':
			v_ligandclass = LigandClass.objects.create(
				name = row['lic_name'],
				description = row['lic_description'],
				)
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_ligandclass = LigandClass.objects.get(name = row['lic_name'])

	''' Ligand '''
	try:
		if row['li_name'] != '':
			v_ligand = Ligand.objects.create(
				ligand_class = v_ligandclass,
				name = row['li_name'],
				description = row['li_description'],
				)
	except IntegrityError as e:
		if match("UNIQUE", str(e)):
			v_ligand = Ligand.objects.get(name = row['li_name'])

	''' Article - ManyToMany relation '''
	article_ids = row['articles'].split(', ')
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
	if row['mechanism'] == 'translation':
		_mechanism = 'TRL'
	elif row['mechanism'] == 'transcription':
		_mechanism = 'TRN'
	elif row['mechanism'] == 'degradation':
		_mechanism = 'DG'

	_effect = 1 if row['effect'] == '+' else '-' if row['effect'] == '-' else 0
	
	v_record = Record.objects.create(
		family = v_ribofamily,
		gene = v_gene,
		organism = v_organism,
		structure = v_structure,
		ligand = v_ligand,
		name = row['switch_name'],
		sequence = row['switch_sequence'],
		genes_under_operon_regulation = row['operon_genes'],
		_3D_structure = row['3d_structure'],
		effect = _effect,
		mechanism = _mechanism,
		strand = row['strand'],
	)
	if row['switch_start'] != 0 or row['switch_end'] != 0:
		v_record.switch_position = Position.objects.create(start = row['switch_start'], end = row['switch_end'])
	if row['tr_start'] != 0 or row['tr_end'] != 0:
		v_record.terminator = Position.objects.create(start = row['tr_start'], end = row['tr_end'])
	if row['pr_start'] != 0 or row['pr_end'] != 0:
		v_record.promoter = Position.objects.create(start = row['pr_start'], end = row['pr_end'])
	
	v_record.save()

	''' Add ManyToMany relations '''
	# Articles #
	for it in v_article:
		v_record.articles.add(it)

for e in Record.objects.all():
	print('\n\n')
	print(e)
	print('\n\n')
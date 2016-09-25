from django.db import models

'''
This are Django models which we use to create our database. Each database table is a class.
ForeignKey, OneToOneField and ManyToManyField refer connections in database.
We use default values temporary - they help us to fill database with sample values.
__str__ functions also will be deleted - they are only for our convenience :)

'''

class Record(models.Model):
	family = models.ForeignKey('RiboFamily', null = True)
	gene = models.OneToOneField('Gene', null = True, related_name = 'gene')
	genes_under_operon_regulation = models.ManyToManyField('Gene', related_name = 'operon_gene') # MANY TO MANY
	organism = models.ForeignKey('Organism', null = True)
	ligand = models.ForeignKey('Ligand', null = True) ###???### Zmieniam na ForeignKey, bo przecież ten sam ligand może należeć do dwóch ryboprzełączników, które mimo takiej samej struktury należą do dwóch różnych organizmów i w bazie danych tworzą dwa różne rekordy.
	structure = models.OneToOneField('Structure', null = True) ###???###
	terminator = models.OneToOneField('Position', null = True, related_name = 'terminator')
	promoter = models.OneToOneField('Position', null = True, related_name = 'promoter')
	switch_position = models.OneToOneField('Position', null = True, related_name = 'switch_position') ###???###
	articles = models.ManyToManyField('Article') # MANY TO MANY
	structure_3d = models.ManyToManyField('Structure3D') # MANY TO MANY ###???###
	
	name = models.CharField('nazwa', max_length = 20)
	sequence = models.TextField('sekwencja') ###???###
	EFFECT_CHOICES = ( 
		('+', 'ACTIVATION'),
		('.', 'UNKNOWN'),
		('-', 'SILECING'),
	)
	effect = models.CharField(max_length = 1, choices = EFFECT_CHOICES, default = '.')
	MECHANISM_CHOICES = (
		('TRN', 'TRANSCRIPTION'),
		('TRL', 'TRANSLATION'),
		('UN', 'UNKNOWN'),
		('DG', 'DEGRADATION'),
	)
	mechanism = models.CharField(max_length = 3, choices = MECHANISM_CHOICES, default = 'UN')
	STRAND_CHOICES = (
		('+', 'LEADING STRAND'),
		('.', 'UNKNOWN'),
		('-', 'LAGGING STRAND'),
	)
	strand = models.CharField(max_length = 1, choices = STRAND_CHOICES, default = '.')

	def __str__(self):
		return 'RECORD: |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| {} {} |{}| |{}| {} {} {}'.format(self.family, self.gene, self.organism, self.ligand, self.structure, self.terminator, self.promoter, self.switch_position, self.articles.all(), self.name, self.sequence, self.genes_under_operon_regulation.all(), self.structure_3d.all(), self.effect, self.mechanism, self.strand)


#class Aptamer(models.Model):
#	sequence =


class Structure(models.Model):
	without_ligand = models.TextField('bez_ligandu')
	with_ligand = models.TextField('z_ligandem')
	predicted = models.TextField('przewidziana')

	def __str__(self):
		return 'Struct: {} {} {}'.format(self.without_ligand, self.with_ligand, self.predicted)


class Article(models.Model):
	pmid = models.IntegerField(primary_key = True) # PubMed ID

	def __str__(self):
		return 'Art: {}'.format(self.pmid)


class Structure3D(models.Model):
	pdbid = models.CharField(max_length = 10, primary_key = True) # Protein Data Bank ID

	def __str__(self):
		return 'Str3D: {}'.format(self.pdbid)


class RiboFamily(models.Model):
	ribo_class = models.ForeignKey('RiboClass', null = True)
	name = models.CharField('nazwa', max_length = 10, primary_key = True) # Default = None, bo ten typ danych zamienia automatycznie None/Null na pusty string (domyślnie default='' dla CharField), przez co nie wywala wyjątku przy wczytywaniu Nulli/Nonów związanego z null = False
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')

	def __str__(self):
		return 'RFam: |{}| {} {} {}'.format(self.ribo_class, self.name, self.description, self.alignment)


class RiboClass(models.Model):
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')

	def __str__(self):
		return 'RCl: {} {} {}'.format(self.name, self.description, self.alignment)


class Gene(models.Model):
	organism = models.ForeignKey('Organism') 
	name = models.CharField('nazwa', max_length = 20, null = False)
	locus_tag = models.CharField(max_length = 15)
	position = models.OneToOneField('Position', null = True, related_name = 'gene_position')
	# Dodać atrybut z numerem chromosomu?
	# Żeby rekord był prawdziwie unikalny trzeba by zrobić primary key na pozycje w genomie, organizm oraz opcjonalnie chromosom
	def __str__(self):
		return 'Gene: |{}| {} {} |{}|'.format(self.organism, self.name, self.locus_tag, self.position)


class Organism(models.Model):
	scientific_name = models.CharField('nazwa_naukowa', max_length = 250, primary_key = True)
	common_name = models.CharField('nazwa_zwyczajowa', max_length = 250)
	accession_number = models.CharField('numer_dostepu', max_length = 15)
	taxonomy_id = models.IntegerField('taxid', default = 0)

	def __str__(self):
		return 'Or: {} {} {}'.format(self.scientific_name, self.common_name, self.accession_number, self.taxonomy_id)


class LigandClass(models.Model):
	name = models.CharField('nazwa', max_length = 20, primary_key = True)
	description = models.TextField('opis')

	def __str__(self):
		return 'LiC: {} {}'.format(self.name, self.description)


class Ligand(models.Model):
	ligand_class = models.ForeignKey('LigandClass', null = True)
	name = models.CharField('nazwa', max_length = 20, primary_key = True)
	description = models.TextField('opis')
	image_name = models.TextField('nazwa pliku')

	def __str__(self):
		return 'Li: |{}| {} {} {}'.format(self.ligand_class, self.name, self.description, self.image_name)


class Position(models.Model):
	start = models.IntegerField(default = 0)
	end = models.IntegerField(default = 0)

	def __str__(self):
		return 'Tr: {} {}'.format(self.start, self.end)
from django.db import models

'''
This are Django models which we use to create our database. Each database table is a class.
ForeignKey, OneToOneField and ManyToManyField refer connections in database.
We use default values temporary - they help us to fill database with sample values.
__str__ functions also will be deleted - they are only for our convenience :)

'''

class Record(models.Model):
	family = models.ForeignKey('RiboFamily', null = True)
	gene = models.OneToOneField('Gene', null = True)
	organism = models.ForeignKey('Organism', null = True)
	ligand = models.ForeignKey('Ligand', null = True) # Zmieniam na ForeignKey, bo przecież ten sam ligand może należeć do dwóch ryboprzełączników, które mimo takiej samej struktury należą do dwóch różnych organizmów i w bazie danych tworzą dwa różne rekordy.
	structure = models.OneToOneField('Structure', null = True)
	terminator = models.OneToOneField('Position', null = True, related_name = 'terminator')
	promoter = models.OneToOneField('Position', null = True, related_name = 'promoter')
	switch_position = models.OneToOneField('Position', null = True, related_name = 'switch_position')
	articles = models.ManyToManyField('Article') # MANY TO MANY

	name = models.CharField('nazwa', max_length = 20, default = 'Undefined')
	sequence = models.TextField('sekwencja', default = 'Undefined')
	genes_under_operon_regulation = models.CharField('geny_pod_regulacja_operonu', max_length = 3000, default = 'Undefined') # Zmienić na ManyToMany?
	_3D_structure = models.TextField('struktura 3D', default = 'Undefined')
	EFFECT_CHOICES = ( 
		(1, 'ACTIVATION'),
		(0, 'UNKNOWN'),
		(-1, 'SILECING'),
	)
	effect = models.IntegerField(choices = EFFECT_CHOICES, default = 0)
	MECHANISM_CHOICES = (
		('TRN', 'TRANSCRIPTION'),
		('TRL', 'TRANSLATION'),
		('UN', 'UNKNOWN'),
		('DG', 'DEGRADATION'),
	)
	mechanism = models.CharField(max_length = 3, choices = MECHANISM_CHOICES, default = 'UN')
	STRAND_CHOICES = (
		('+', 'LEADING STRAND'),
		('-', 'LAGGING STRAND'),
		('0', 'UNKNOWN'),
	)
	strand = models.CharField(max_length = 1, choices = STRAND_CHOICES, default = '0')

	def __str__(self):
		return 'RECORD: |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| |{}| {} {} {} {} {} {} {}'.format(self.family, self.gene, self.organism, self.ligand, self.structure, self.terminator, self.promoter, self.switch_position, self.articles.all(), self.name, self.sequence, self.genes_under_operon_regulation, self._3D_structure, self.effect, self.mechanism, self.strand)


class Structure(models.Model):
	without_ligand = models.TextField('bez_ligandu', default = 'Undefined')
	with_ligand = models.TextField('z_ligandem', default = 'Undefined')
	predicted = models.TextField('przewidziana', default = 'Undefined')

	def __str__(self):
		return 'Struct: {} {} {}'.format(self.without_ligand, self.with_ligand, self.predicted)


class Article(models.Model):
	pmid = models.IntegerField(primary_key = True)

	def __str__(self):
		return 'Art: {}'.format(self.pmid)


class RiboFamily(models.Model):
	ribo_class = models.ForeignKey('RiboClass', null = True)
	name = models.CharField('nazwa', max_length = 10, primary_key = True) # Default = None, bo ten typ danych zamienia automatycznie None/Null na pusty string (domyślnie default='' dla CharField), przez co nie wywala wyjątku przy wczytywaniu Nulli/Nonów związanego z null = False
	description = models.TextField('opis', default = '')
	alignment = models.TextField(default = 'Undefined')

	def __str__(self):
		return 'RFam: |{}| {} {} {}'.format(self.ribo_class, self.name, self.description, self.alignment)


class RiboClass(models.Model):
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis', default = 'None')
	alignment = models.TextField(default = 'Undefined')

	def __str__(self):
		return 'RCl: {} {} {}'.format(self.name, self.description, self.alignment)

class Gene(models.Model): # Duplikacja genów w jednym organizmie. Jeden gen może posiadać więcej niż jedną nazwę ; Co powinno być kluczem głównym? Tylko accession_number, wszystko lub nic?
# Tymczasowo dopóki nie ogarnę wczytywania accession number kluczem głównym jest domyślny atrybut ID.
	organism = models.ForeignKey('Organism') 
	name = models.CharField('nazwa', max_length = 20, null = False)
	accession_number = models.CharField('numer_dostepu', max_length = 15, default = 'Undefined') # primary_key = True, Tu powinien być klucz główny, ale wczytując z pliku nie ma podanego numeru dostępu, więc na razie usuwam. Tymczasowo.
	position = models.OneToOneField('Position', null = True, related_name = 'gene_position')
	taxonomy_id = models.IntegerField('taxid', default = 0)
	# Dodać atrybut z numerem chromosomu?
	# Żeby rekord był prawdziwie unikalny trzeba by zrobić primary key na pozycje w genomie, organizm oraz opcjonalnie chromosom
	def __str__(self):
		return 'Gene: |{}| {} {} |{}| {}'.format(self.organism, self.name, self.accession_number, self.position, self.taxonomy_id)


class Organism(models.Model):
	scientific_name = models.CharField('nazwa_naukowa', max_length = 250, primary_key = True)
	common_name = models.CharField('nazwa_zwyczajowa', max_length = 250, default = 'Undefined')
	accession_number = models.CharField('numer_dostepu', max_length = 15, default = 'Undefined') # Czy to jest potrzebne? Z jakiej bazy to pobrać? NCBI Genome?

	def __str__(self):
		return 'Or: {} {} {}'.format(self.scientific_name, self.common_name, self.accession_number)

class LigandClass(models.Model):
	name = models.CharField('nazwa', max_length = 20, primary_key = True)
	description = models.TextField(default = 'None')

	def __str__(self):
		return 'LiC: {} {}'.format(self.name, self.description)

class Ligand(models.Model):
	ligand_class = models.ForeignKey('LigandClass', null = True)
	name = models.CharField('nazwa', max_length = 20, primary_key = True)
	#OBRAZEK - DOPYTAC ?
	description = models.TextField('opis', default = 'None')

	def __str__(self):
		return 'Li: |{}| {} {}'.format(self.ligand_class, self.name, self.description)

class Position(models.Model):
	start = models.IntegerField(default = 0)
	end = models.IntegerField(default = 0)

	def __str__(self):
		return 'Tr: {} {}'.format(self.start, self.end)
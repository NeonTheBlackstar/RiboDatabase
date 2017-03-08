from django.db import models

'''
This are Django models which we use to create our database. Each database table is a class.
ForeignKey, OneToOneField and ManyToManyField refer connections in database.
We use default values temporary - they help us to fill database with sample values.
'''

class Record(models.Model):
	''' Encja Switch podlinkowana '''
	family = models.ForeignKey('RiboFamily', null = True)
	gene = models.OneToOneField('Gene', null = True, related_name = 'gene')
	genes_under_operon_regulation = models.ManyToManyField('Gene', related_name = 'operon_gene') # MANY TO MANY
	terminator = models.OneToOneField('Position', null = True, related_name = 'terminator')
	promoter = models.OneToOneField('Position', null = True, related_name = 'promoter')
	articles = models.ManyToManyField('Article', related_name = 'article') # MANY TO MANY
	
	name = models.CharField('nazwa', max_length = 20)
	#riboswitch_id = models.CharField('id', max_length = 20, primary_key = True)
	#id dodac
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
	mechanism_confirmation = models.ForeignKey('Article', related_name = 'confirmation', null = True)

	def __str__(self):
		return 'RECORD: |{}| |{}| |{}| |{}| |{}| |{}| {} |{}| {} {} |{}|'.format(self.family, self.aptamer_set.all(), self.gene, self.terminator, self.promoter, self.articles.all(), self.name, self.genes_under_operon_regulation.all(), self.effect, self.mechanism, self.mechanism_confirmation)


class Aptamer(models.Model): #14 dodaję nową encję
	sequence = models.TextField('sekwencja')
	position = models.OneToOneField('Position', null = True, related_name = 'aptamer_position')
	structure = models.OneToOneField('Structure2D', null = True)
	switch = models.ForeignKey('Record')#, related_name = "aptamer")
	# aptamer_id = models.CharField('id', max_length = 20, primary_key = True)
	# RDB000008.1?
	# pole id aptameru w ryboswitchu

	def __str__(self):
		return 'Apt: {} |{}| |{}|'.format(self.sequence, self.position, self.structure)


class Structure2D(models.Model):
	without_ligand = models.TextField('bez_ligandu')
	with_ligand = models.TextField('z_ligandem')
	predicted = models.TextField('przewidziana')

	def __str__(self):
		return 'Struct: {} {} {}'.format(self.without_ligand, self.with_ligand, self.predicted)


class Article(models.Model):
	pmid = models.IntegerField(primary_key = True)

	def __str__(self):
		return 'Art: {}'.format(self.pmid)


class Structure3D(models.Model):
	pdbid = models.CharField(max_length = 10, primary_key = True) # Protein Data Bank ID
	ribo_family = models.ForeignKey('RiboFamily')

	def __str__(self):
		return 'Str3D: {}'.format(self.pdbid)


class RiboFamily(models.Model): # w record taka sama nazwa !
	''' RiboClass podlinkowane '''
	''' Structure3D podlinkowane '''
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')
	ligands = models.ManyToManyField('Ligand')
	#ligand = models.ForeignKey('Ligand', null = True)

	def __str__(self):
		return 'RFam: |{}| {} {} {} |{}|'.format(self.riboclass_set.all(), self.name, self.description, self.alignment, self.ligands.all())#, self.structure3D.all())


class RiboClass(models.Model):
	ribo_family = models.ForeignKey('RiboFamily', null = True)
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')

	def __str__(self):
		return 'RCl: {} {} {}'.format(self.name, self.description, self.alignment)


class Gene(models.Model):
	organism = models.ForeignKey('Organism', null = True) 
	name = models.CharField('nazwa', max_length = 20, null = False)
	locus_tag = models.CharField(max_length = 15)
	position = models.OneToOneField('Position', null = True, related_name = 'gene_position')
	def __str__(self):
		return 'Gene: |{}| {} {} |{}|'.format(self.organism, self.name, self.locus_tag, self.position)


class Organism(models.Model):
	scientific_name = models.CharField('nazwa_naukowa', max_length = 250, primary_key = True)
	common_name = models.CharField('nazwa_zwyczajowa', max_length = 250)
	accession_number = models.CharField('numer_dostepu', max_length = 15)
	taxonomy = models.ForeignKey('Taxonomy', null = True)

	def __str__(self):
		return 'Or: {} {} {} |{}|'.format(self.scientific_name, self.common_name, self.accession_number, self.taxonomy)


class Taxonomy(models.Model):
	name = models.CharField('nazwa', max_length = 20, null = False)
	taxonomy_id = models.IntegerField('taxid', default = 0)#, primary_key = True)
	parent = models.ForeignKey('Taxonomy', null = True)

	def __str__(self):
		return 'Tax: {} {}'.format(self.name, self.taxonomy_id)
	# do napisania skrypt, ktory bedzie to ladowal do bazy rekurencyjnie - To zrobi Szymon


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
	# baza ligandow

	def __str__(self):
		return 'Li: |{}| {} {} {}'.format(self.ligand_class, self.name, self.description, self.image_name)


class Position(models.Model):
	start = models.IntegerField(default = 0)
	end = models.IntegerField(default = 0)
	location = models.TextField('opis')
	STRAND_CHOICES = (
		('+', 'LEADING STRAND'),
		('.', 'UNKNOWN'),
		('-', 'LAGGING STRAND'),
	)
	strand = models.CharField(max_length = 1, choices = STRAND_CHOICES, default = '.')

	def __str__(self):
		return 'Pos: {} {} |{}| {}'.format(self.start, self.end, self.location, self.strand)
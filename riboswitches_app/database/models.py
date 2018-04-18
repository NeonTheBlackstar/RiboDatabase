from django.db import models

'''
This are Django models which we use to create our database. Each database table is a class.
ForeignKey, OneToOneField and ManyToManyField refer connections in database.
We use default values temporary - they help us to fill database with sample values.
'''

class Record(models.Model):
	family = models.ForeignKey('RiboFamily', null = True)
	gene = models.OneToOneField('Gene', null = True, related_name = 'gene')
	genes_under_operon_regulation = models.ManyToManyField('Gene', related_name = 'operon_gene')
	terminator = models.OneToOneField('Position', null = True, related_name = 'terminator')
	promoter = models.OneToOneField('Position', null = True, related_name = 'promoter')
	shinedalgarno = models.OneToOneField('Position', null = True, related_name = 'shinedalgarno')
	articles = models.ManyToManyField('Article', related_name = 'article')
	sequence = models.TextField('sekwencja')
	
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
		return 'RECORD: |{}| |{}| |{}| |{}| |{}| |{}| |{}| {} {} |{}| {}'.format(self.family, self.aptamer_set.all(), self.gene, self.terminator, self.promoter, self.articles.all(), self.genes_under_operon_regulation.all(), self.effect, self.mechanism, self.mechanism_confirmation, self.sequence)

	def name(self):
		return "RS{}".format((str(self.id).zfill(8)))

class Aptamer(models.Model):
	position = models.OneToOneField('Position', null = True, related_name = 'aptamer_position')
	structure = models.OneToOneField('Structure2D', null = True)
	switch = models.ForeignKey('Record')

	def __str__(self):
		return 'Apt: |{}| |{}|'.format(self.position, self.structure)


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
	pdbid = models.CharField(max_length = 10, primary_key = True)
	ribo_class = models.ForeignKey('RiboClass')

	def __str__(self):
		return 'Str3D: {}'.format(self.pdbid)


class RiboFamily(models.Model):
	ribo_class = models.ForeignKey('RiboClass', null = True)
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')

	def __str__(self):
		return 'RFam: {} {} {} |{}|'.format(self.name, self.description, self.alignment, self.ribo_class)


class RiboClass(models.Model):
	# Accesion number???
	name = models.CharField('nazwa', max_length = 10, primary_key = True)
	description = models.TextField('opis')
	alignment = models.TextField('dopasowanie')
	ligands = models.ManyToManyField('Ligand')

	def __str__(self):
		return 'RCl: {} {} {} |{}|'.format(self.name, self.description, self.alignment, self.ligands.all())


class Gene(models.Model):
	organism = models.ForeignKey('Organism', null = True) 
	name = models.CharField('nazwa', max_length = 20, null = False)
	locus_tag = models.CharField(max_length = 15)
	position = models.OneToOneField('Position', null = True, related_name = 'gene_position')
	def __str__(self):
		return 'Gene: |{}| {} {} |{}|'.format(self.organism, self.name, self.locus_tag, self.position)


class Organism(models.Model):
	scientific_name = models.CharField('nazwa_naukowa', max_length = 250)
	common_name = models.CharField('nazwa_zwyczajowa', max_length = 250)
	accession_number = models.CharField('numer_dostepu', max_length = 30)
	build_id = models.CharField('numer_dostepu', max_length = 30, primary_key = True)
	taxonomy = models.OneToOneField('Taxonomy', null = True)

	def __str__(self):
		return 'Or: {} {} {} {} |{}|'.format(self.scientific_name, self.common_name, self.accession_number, self.build_id, self.taxonomy)


class Taxonomy(models.Model):
	name = models.CharField('nazwa', max_length = 20, null = True)
	taxonomy_id = models.IntegerField('taxid', default = 0, primary_key = True)
	parent = models.ForeignKey('Taxonomy', null = True)

	def __str__(self):
		return 'Tax: {} {} |{}|'.format(self.name, self.taxonomy_id, self.parent)


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
	location = models.TextField('opis')
	score = models.FloatField(default = 0.0)
	STRAND_CHOICES = (
		('+', 'LEADING STRAND'),
		('.', 'UNKNOWN'),
		('-', 'LAGGING STRAND'),
	)
	strand = models.CharField(max_length = 1, choices = STRAND_CHOICES, default = '.')

	def __str__(self):
		return "Start: {}, End: {}, Score: {}, Location: {}, Strand: {}".format(self.start, self.end, self.score, self.location, self.strand)

from django.db import models

'''

This are Django models which we use to create our database. Each database table is a class.
ForeignKey, OneToOneField and ManyToManyField refer connections in database.
We use default values temporary - they help us to fill database with sample values.
__str__ functions also will be deleted - they are only for our convenience :)

'''

class Record(models.Model):
	#By setting the parameter null to value True we can insert None values to database
	family = models.ForeignKey('RiboFamily', null = True)
	gene = models.OneToOneField('Gene', null = True)
	structure = models.ForeignKey('Structure', null = True)
	organism = models.ForeignKey('Organism', null = True)
	ligand = models.OneToOneField('Ligand', null = True)
	terminator = models.OneToOneField('Terminator', null = True)
	promoter = models.OneToOneField('Promoter', null = True)
	article = models.ManyToManyField('Article')

	name = models.CharField('nazwa', max_length = 20, default = 'UNKNOWN')
	sequence = models.TextField('sekwencja', default = 'NONE')
	start_pos = models.IntegerField(default = 0)
	end_pos = models.IntegerField(default = 0)
	genes_under_operon_regulation = models.CharField('geny_pod_regulacja_operonu', max_length = 3000, default = 'NONE')
	_3D_structure = models.TextField('struktura 3D', default = 'NONE')
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


class Structure(models.Model):
	without_ligand = models.TextField('bez_ligandu', default = 'NONE')
	with_ligand = models.TextField('z_ligandem', default = 'NONE')
	predicted = models.TextField('przewidziana', default = 'NONE')


class Article(models.Model):
	pmid = models.IntegerField(default = 0, primary_key = True)


class RiboFamily(models.Model):
	ribo_class = models.ForeignKey('RiboClass', null = True)
	name = models.CharField('nazwa', max_length = 10, default = 'NONE')
	description = models.TextField('opis', default = 'NONE')
	alignment = models.TextField(default = 'NONE')

	def __str__(self):
		return '{} {} {} {}'.format(self.ribo_class, self.name, self.description, self.alignment)


class RiboClass(models.Model):
	name = models.CharField('nazwa', max_length = 10)
	description = models.TextField('opis', default = 'NONE')
	alignment = models.TextField(default = 'NONE')

	def __str__(self):
		return '{} {} {}'.format(self.name, self.description, self.alignment)


class Gene(models.Model):
	organism = models.ManyToManyField('Organism')
	accession_number = models.CharField('numer_dostepu', max_length = 15, primary_key = True, default = 'NONE')
	name = models.CharField('nazwa', max_length = 20, default = 'NONE')
	start_pos = models.IntegerField(default = 0)
	end_pos = models.IntegerField(default = 0)


class Organism(models.Model):
	accession_number = models.CharField('numer_dostepu', max_length = 15, primary_key = True, default = 'NONE')
	taxid = models.IntegerField(default = 0)
	common_name = models.CharField('nazwa_zwyczajowa', max_length = 250, default = 'NONE')
	scientific_name = models.CharField('nazwa_naukowa', max_length = 250, default = 'NONE')
	fasta_seq = models.TextField(default = 'NONE') ######################################################


class Ligand_class(models.Model):
	name = models.CharField('nazwa', max_length = 20, default = 'NONE')
	description = models.TextField(default = 'NONE')


class Ligand(models.Model):
	ligand_class = models.ForeignKey('Ligand_class', null = True)
	name = models.CharField('nazwa', max_length = 20, default = 'NONE')
	#OBRAZEK - DOPYTAC ?
	description = models.TextField('opis', default = 'NONE')

	def __str__(self):
		return '{} {}'.format(self.ligand_class, self.name, self.description)


class Terminator(models.Model):
	start = models.IntegerField(default = 0)
	end = models.IntegerField(default = 0)

	def __str__(self):
		return '{} {}'.format(self.start, self.end)


class Promoter(models.Model):
	start = models.IntegerField(default = 0)
	end = models.IntegerField(default = 0)

	def __str__(self):
		return '{} {}'.format(self.start, self.end)

from django.db import models


class Record(models.Model):
	family = models.ForeignKey('RiboFamily')
	gene = models.OneToOneField('Gene')
	structure = models.ForeignKey('Structure')
	organism = models.ForeignKey('Organism')
	ligand = models.OneToOneField('Ligand')
	terminator = models.OneToOneField('Terminator')
	promoter = models.OneToOneField('Promoter')
	article = models.ManyToManyField('Article')
	name = models.CharField('nazwa', max_length=20)
	sequence = models.TextField('sekwencja')
	start_pos = models.IntegerField()
	end_pos = models.IntegerField()
	genes_under_operon_regulation = models.CharField('geny_pod_regulacja_operonu', max_length=30)#DOPYTAC
	_3D_structure = models.TextField('struktura 3D')
	EFFECT_CHOICES = ( #DO WERYFIKACJI 
		(1, 'ACTIVATION'),
		(0, 'UNKNOWN'),
		(-1, 'SILECING'),
	)
	effect = models.IntegerField(choices=EFFECT_CHOICES)
	MECHANISM_CHOICES = (
		('TRN', 'TRANSCRIPTION'),
		('TRL', 'TRANSLATION'),
		('UN', 'UNKNOWN'),
		('DG', 'DEGRADATION'),
	)
	mechanism = models.CharField(max_length=3, choices=MECHANISM_CHOICES)
	STRAND_CHOICES = (
		('+', 'LEADING STRAND'),
		('-', 'LAGGING STRAND'),
	)
	strand = models.CharField(max_length=1, choices=STRAND_CHOICES)


class Structure(models.Model):
	without_ligand = models.TextField('bez_ligandu')
	with_ligand = models.TextField('z_ligandem')
	predicted = models.TextField('przewidziana')


class Article(models.Model):
	pmid = models.IntegerField()


class RiboFamily(models.Model):
	ribo_class = models.ForeignKey('RiboClass', null=True)
	name = models.CharField('nazwa', max_length=10)
	description = models.TextField('opis')
	alignment = models.TextField()

	def __str__(self):
		return '{} {} {} {}'.format(self.ribo_class, self.name, self.description, self.alignment)


class RiboClass(models.Model):
	name = models.CharField('nazwa', max_length=10)
	description = models.TextField('opis')
	alignment = models.TextField()

	def __str__(self):
		return '{} {} {}'.format(self.name, self.description, self.alignment)


class Gene(models.Model):
	organism = models.ManyToManyField('Organism')
	accession_number = models.CharField('numer_dostepu', max_length=15, primary_key=True)
	name = models.CharField('nazwa', max_length=20)
	start_pos = models.IntegerField()
	end_pos = models.IntegerField()


class Organism(models.Model):
	accession_number = models.CharField('numer_dostepu', max_length=15, primary_key=True)
	taxid = models.IntegerField()
	common_name = models.CharField('nazwa_zwyczajowa', max_length=250)
	scientific_name = models.CharField('nazwa_naukowa', max_length=250)
	fasta_seq = models.TextField() ######################################################


class Ligand_class(models.Model):
	name = models.CharField('nazwa', max_length=20)
	description = models.TextField()


class Ligand(models.Model):
	ligand_class = models.ForeignKey('Ligand_class')
	name = models.CharField('nazwa', max_length=20)
	#OBRAZEK - DOPYTAC ?
	description = models.TextField('opis')

	def __str__(self):
		return '{} {}'.format(self.ligand_class, self.name, self.description)


class Terminator(models.Model):
	start = models.IntegerField()
	end = models.IntegerField()

	def __str__(self):
		return '{} {}'.format(self.start, self.end)


class Promoter(models.Model):
	start = models.IntegerField()
	end = models.IntegerField()

	def __str__(self):
		return '{} {}'.format(self.start, self.end)
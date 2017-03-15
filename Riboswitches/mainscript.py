from BCBio import GFF
from glob import glob
import os
import re
import sys
import linecache
sys.path.insert(0, './Programs/shine-dalgarno')
import __init__
import sd2
import new_sd2
from datetime import datetime, timedelta
from time import sleep, localtime, strftime
# python3 mainscript.py NC_000964.3

# Sprawdzic czy ktorys program wymaga instalacji TYLKO DO SD

### HELPER FUNCTIONS ###

# Pole do optymalizacji: już w nagłówku fasta zawrzeć wszystkie potrzebne info LUB nie otwierać i nie zamykać parsera GFF przy kazdym aptamerze, tylko zrobić to raz w jednej funkcji.

# Czy gene_biotype tylko protein coding?
# BSU11010

# dorobić dla minus ZROBIONE

# Wyszło więcej aptamerów niż wcześniej dla całego fasta

# Zrobic bedy z widelkami ZROBIONE

# Gen BSU20040 nie dziala! ZROBIONE

# Między window a results jest przesunięcie o 1 nukleotyd! Ogarnąć!

def getGeneInfo(locus_tag, gff):
	handle = open(gff)
	for record in GFF.parse(handle): # We have only one record in the file, so the loop is uneccessary
		for feature in record.features:
			if feature.type == 'gene' and feature.qualifiers['locus_tag'][0] == locus_tag:
				start = feature.location.start # Automatically substract 1, so it matches ID array notation
				end = feature.location.end
				strand = '+' if feature.strand == 1 else '-'

				handle.close()
				return {'start': start, 'end': end, 'strand': strand}
	return None

def getAbsolutePositions(genome):
	f = open("./Results/{0}.result".format(genome))
	out = open("./Results/apt.bed", 'w')


	for line in f:
		line = line.strip().split('\t')

		locus_tag = line[5].split('|')[0]
		aptamer_start = int(line[1])
		aptamer_end = int(line[2])
		before_interval = int(line[5].split('|')[1])
		gene = getGeneInfo(locus_tag, "./Genomes/{0}.gff".format(genome)) 

		if gene['strand'] == '+':
			before_pos = gene['start'] - before_interval
			start = before_pos + aptamer_start - 1 # -1 because counting starts from 1
			end = before_pos + aptamer_end - 1 # -1 because counting starts from 1
			#out.write("{}\t{}\t{}\t{}\n".format(locus_tag, start, end, gene['strand']))
			out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format('chr', start, end, locus_tag, '0', gene['strand']))

		elif gene['strand'] == '-':
			before_pos = gene['end'] + before_interval
			# Invert start and end
			start = before_pos - aptamer_end - 1 # -1 because counting starts from 1
			end = before_pos - aptamer_start - 1 # -1 because counting starts from 1
			out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format('chr', start, end, locus_tag, '0', gene['strand']))

	f.close()
	out.close()


########################

def aptamers(genome):
	#Aptamery - Jakub
	lista = []
	lista = os.listdir('Alignments')
	counter = 0

	finalFile = open("./Results/{0}.result".format(genome), "w")

	''' Sort gff file ascending on strand + and descending on strand - for easier calculations '''
	# Sorted by strand
	os.system("tail -n +8 ./Genomes/{0}.gff | head -n -1 | sort -t \"\t\" -k7,7 -k4,4n > ./Genomes/byStrand.gff".format(genome)) # Mógblym tego nie sortowac i przejsc tylko raz przez plik
	# Remove previous file if there's any
	os.system('rm ./Genomes/{0}_sorted.gff > /dev/null 2>&1'.format(genome))
	# Sorted by ascending start position on strand +
	os.system("awk '$7 == \"+\"' ./Genomes/byStrand.gff | sort -k4,4n >> ./Genomes/{0}_sorted.gff".format(genome))
	# Sorted by descending start position on strand -
	os.system("awk '$7 == \"-\"' ./Genomes/byStrand.gff | sort -k5,5nr >> ./Genomes/{0}_sorted.gff".format(genome))

	''' Create multiple fasta file of propable aptamer regions '''
	new_sd2.getFasta("-gff", "./Genomes/{0}_sorted.gff".format(sys.argv[1]), "-fasta", "./Genomes/{0}.fasta".format(genome), "-before", 500, "-after", 200, "-aptamer", 50, "-bed", True)

	for i in range(0, len(lista)):
		
		os.system("./Programs/cmsearch --toponly -o ./Results/processing.txt ./Alignments/{0} ./aptamer_windows.fasta".format(lista[i], genome))

		processingfile = open("./Results/processing.txt", "r")

		for line in processingfile:
			temp = line.strip().split()
			if len(temp) > 5:
				if temp[1] == "!" and temp[5].startswith("BSU"): # Ten warunek nie dziala
					if temp[8] == "-":
						finalFile.write("{5}\t{1}\t{0}\t{2}_{0}\t{3}\t{4}\n".format(temp[6], temp[7], lista[counter][0:-3], temp[3], temp[5], genome))
					else:
						finalFile.write("{5}\t{0}\t{1}\t{2}_{0}\t{3}\t{4}\n".format(temp[6], temp[7], lista[counter][0:-3], temp[3], temp[5], genome))
		counter = counter + 1
		processingfile.close()

	finalFile.close()

	getAbsolutePositions(genome) # zajmuje az 20 sekund!
	
	os.system("rm ./Results/processing.txt")
	os.system("rm ./aptamer_windows.fasta")
	os.system('rm ./Genomes/byStrand.gff')
	#os.system('rm ./Genomes/{0}_sorted.gff'.format(genome))

	os.system('sort -k2,2n ./Results/{0}.result -o ./Results/{0}.sorted'.format(genome))
	os.system('mv ./Results/{0}.sorted ./Results/{0}.result'.format(genome))
	#os.system('rm ./Results/{0}.sorted'.format(genome))

	print("debug") ### TU SKONCZYLEM
	return


def promoters(
	genome_id = sys.argv[1], 									# Genome ID
	genome_fasta = './Genomes/{}.fasta'.format(sys.argv[1]),	# Genome fasta file path
	window = '100', 											# Window size for the upstream region to be compared
	gccontent = 'default'										# GC-content of the whole genome
	):
	
	# Bede musial podac GC% calego analizowanego genomu. Do wyciągnięcia z Ensmbla. Mają API

	os.system('echo \'{0}\n{1}\n{2}\' | ./Programs/PromPredict_genome_V1'.format(genome_fasta, window, gccontent))

	PP_output_path = glob('./*_PPde.txt')[0]
	with open('./Results/{0}.promoters.bed'.format(genome_id), 'w') as result, open(PP_output_path) as PPout:
		for line in PPout:
			if not line.startswith('#'):
				temp_list = line.strip().split('\t')
				start = temp_list[2] 					#pozycja startu
				end = temp_list[3] 						#pozycja konca
				_id = start 							#id = start
				level = temp_list[-1][-1] 				#jakosc
				result.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(genome_id, start, end, _id, level))

	os.system('rm ./*_PPde.txt')
	os.system('rm ./*_stb.txt')
	os.system('rm ./*_GCstat.txt')


def terminators(genome):
	#Terminatory - Pawel
	fh1 = open('./Genomes/{0}.gff'.format(genome))
	fh2 = open('temp.gff', 'w')
	semaphore=0
	for line in fh1:
		temp = line.split('\t')
		if temp[0][0]!='#':
			if (temp[2]=='region' and semaphore==0):
				semaphore=1
			else:
				fh2.write(line)
	fh1.close()
	fh2.close()
	os.system('bedtools closest -s -D a -io -iu -a ./Results/{0}.aptamers.bed -b temp.gff > bed_output.txt'.format(genome))
	#os.system('rm temp.gff')

	fh1 = open('bed_output.txt')
	fh2 = open('./Results/{0}.ptt'.format(genome), 'w')

	fh2.write('Location\tStrand\tLength\tPID\tGene\tSynonym\tCode\tCOG\tProduct\n\n\n')

	# Ptt creation #
	for line in fh1:
		temp = line.split('\t')
		if (temp[8]=='gene'):
			location1=temp[1]+'..'+temp[2]
			location2=temp[9]+'..'+temp[10]
			strand=temp[5]
			length1=str(int(temp[2])-int(temp[1])+1)
			length2=str(int(temp[10])-int(temp[9])+1)
			gene1 = temp[3]
			name = re.search(r'Name=[^;^\n]*',temp[14])
			if (str(name) == 'None'):
				gene2 = '-'
			else:
				gene2 = name.group()
				gene2 = gene2[5:]
				locus_tag = re.search(r'locus_tag=[^;^\n]*',temp[14])
				if (str(locus_tag) == 'None'):
					synonym = '-'
				else:
					synonym = locus_tag.group()
					synonym = synonym[10:]
		if (temp[8]=='CDS' or temp[8]=='exon'):
			protein_id = re.search(r'protein_id=[^;^\n]*',temp[14])
			if (str(protein_id) == 'None'):
				pid = '-'
			else:
				pid = protein_id.group()
				pid = pid[11:]
				product_name = re.search(r'product=[^;^\n]*',temp[14])
				if (str(product_name) == 'None'):
					product = '-'
				else:
					product=product_name.group()
					product=product[8:]
			fh2.write(location1+'\t'+strand+'\t'+length1+'\t'+pid+'\t>'+gene1+'\t>'+gene1+'\t-\t-\t'+gene2+';'+synonym+'\n')
			fh2.write(location2+'\t'+strand+'\t'+length2+'\t'+pid+'\t'+gene2+'\t'+synonym+'\t-\t-\t'+product+'\n')
	#os.system('rm bed_output.txt')
	# End #

	### DEBUG LINE ###
	print("DEBUG")
	input()
	### ###

	fh1.close()
	fh2.close()
	
	fh1 = open('./Genomes/{0}.fasta'.format(genome))
	fh2 = open('sequence.fasta', 'w')
	for line in fh1:
		if line[0]=='>':
			fh2.write('>{0}\n'.format(genome))
		else:
			fh2.write(line)
	
	os.system('transterm -p ./Programs/transterm/expterm.dat sequence.fasta ./Results/{0}.ptt > output.tt'.format(genome))
	os.system('rm sequence.fasta')

	fh1 = open('output.tt')
	fh2 = open('./Results/{0}.terminators.bed'.format(genome), 'w')

	data = []
	RF = []
	terminators_tt = []
	terminators_bed = []

	for line in fh1:
		if (line != '\n'):
			data.append(line)

	counter=0
	for line in data:
		temp = line.split()
		if (line[0][0] == '>' and temp[4] == '+'):
				end_RF = temp[3]
				for i in range(counter+1,len(data)):
					check = data[i].split()
					if (check[0] == 'TERM'):
						start_term = check[2]
						distance = int(start_term)-int(end_RF)
						if (distance<150):
							RF.append(line[1:])
							terminators_tt.append(data[i])
							break
		if (line[0][0] == '>' and temp[4] == '-'):
				start_RF = temp[3]
				j=counter-1
				for i in range(0,counter):
					check = data[j].split()
					if (check[0] == 'TERM'):
						end_term = check[2]
						distance = int(start_RF)-int(end_term)
						if (distance<150):
							RF.append(line[1:])
							terminators_tt.append(data[j])
							break
					j=j-1			
		counter=counter+1

	counter=0
	for line in terminators_tt:
		temp1 = line.split()
		temp2 = RF[counter].split()
		counter=counter+1	
		if (temp1[5] == '+'): 
			fh2.write('{0}\t'.format(genome)+temp1[2]+'\t'+temp1[4]+'\t'+temp2[0]+';'+temp2[6]+'\t'+temp1[7]+'\t'+temp1[5]+'\n')
		if (temp1[5] == '-'): 
			fh2.write('{0}\t'.format(genome)+temp1[4]+'\t'+temp1[2]+'\t'+temp2[0]+';'+temp2[6]+'\t'+temp1[7]+'\t'+temp1[5]+'\n')

	fh1.close()
	fh2.close()
	
	os.system('rm output.tt')


def bedtools(genome):
	#ignore overlaps, ignore downstream, signed dist. w. r. t. A's strand
	os.system('bedtools closest -io -id -D a -a ./Results/{0}.aptamers.bed -b ./Results/{0}.promoters.bed > ./Results/{0}.bedAP.txt'.format(genome))


def comparison(genome, distance_P = 150, distance_T = 150, distance_SD = 200):
	#format: genome start_R end_R name_R strand_R start_P end_P distance_P start_T end_T strand_T distance_T start_SD end_SD strand_SD distance_SD gene_annotation type_of_mechanism
	#default distance: P = 150, T = 150, SD = 200 
	final = open('./Results/{0}.final.txt'.format(genome), 'w')
	aptamers = open('./Results/{0}.bedAP.txt'.format(genome), 'r')
	for lineA in aptamers:
		P_exist = False
		T_exist = False
		SD_exist = False
		tempA = lineA.split()
		final.write('{0}\t{1}\t{2}\t{3}\t{4}\t'.format(genome, tempA[1], tempA[2], tempA[3], tempA[5]))
		if int(tempA[11]) >= (-(int(distance_P))):
			final.write('{0}\t{1}\t{2}\t'.format(tempA[7], tempA[8], tempA[11]))
			P_exist = True
		else:
			final.write('---\t---\tNo_P\t')
		terminators = open('./Results/{0}.bedAT.txt'.format(genome), 'r')
		for lineT in terminators:
			tempT = lineT.split()
			if int(tempT[13]) <= distance_T and tempT[3] == tempA[3]:
				final.write('{0}\t{1}\t{2}\t{3}\t'.format(tempT[7], tempT[8], tempT[12], tempT[13]))
				T_exist = True
				break
		else:
			final.write('---\t---\t---\tNo_T\t')
		terminators.close()
		'''
		sdsequence = open('./Results/{0}.bedASD.txt'.format(genome))
		for lineSD in sdsequence:
			tempSD = lineSD.split()
			if ...
				...
				break
		else:
			final.write(...)
		sdsequence.close()
		'''
		
		if P_exist and T_exist:
			final.write('Termination\n')
		if P_exist and not T_exist and not SD_exist:
			final.write('Unknown\n')
		if P_exist and SD_exist and not T_exist:
			final.write('Translation\n')
		if not P_exist and T_exist:
			final.write('Termination\n')
		if not P_exist and not T_exist:
			final.write('Unknown\n')

a = datetime.now()
aptamers(sys.argv[1])
#promoters()
#terminators(sys.argv[1])
#__init__.runShineDalAnalysis(sys.argv[1], True) # If set true, then meme will be runed
#bedtools(sys.argv[1])
#comparison(sys.argv[1])

print('Done ' + str(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())))
b = datetime.now()
c = b - a
print("{} seconds {} microseconds".format(c.seconds, c.microseconds))


'''
Tabela: aptamery: scory, pozeycje, sekwencje aptamrow
promotory: pozycje, scory,
terminatory: pozycje, scory

DRS0000001
'''
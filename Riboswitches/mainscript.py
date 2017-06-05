from BCBio import GFF
from glob import glob
import os
import re
import sys
import linecache
import subprocess
sys.path.insert(0, './Programs/shine-dalgarno')
import __init__
import sd2
import new_sd2
from datetime import datetime, timedelta
from time import sleep, localtime, strftime
# python3 mainscript.py NC_000964.3

### HELPER FUNCTIONS ###

def makeAptamersBed(genome):
	os.system("awk \'BEGIN {OFS = \"\\t\"}; {print \"chr\", $7, $8, $2, $9, $5}\' ./Results/"+genome+".result > ./Results/apt.bed")

#chr, {6}, {7}, {1}, {8}, {4} // liczone od 0

def makePromotersBed(genome):
	os.system("awk \'BEGIN {OFS = \"\\t\"}; {print \"chr\", $11, $12, $2, 0, $5}\' ./Results/"+genome+".result > ./Results/prom.bed")


#chr, {10}, {11}, {9}, 0, {4} // liczone od 0

'''
"awk  \'BEGIN {OFS = \"\\t\"}; {if({0} == "scientific_name") print $5, '\t' ,$3;}\'".format('xD')
'''

def createPromoterFilter(result_file):
	filter_list = []
	with open(result_file) as result_handle:
		for line in result_handle:
			line = line.strip().split('\t')
			filter_list.append(line[1]) # Append locus tag
	return(filter_list)

### END ###


def aptamers(
	genome,				# Genome ID
	e_value = 0.001, 	# Maximum e-value for aptamer to ?evaluate?
	):

	lista = []
	lista = os.listdir('Alignments')

	finalFile = open("./Results/{0}.result".format(genome), "w")

	''' Sort gff file ascending on strand + and descending on strand - for easier calculations '''
	# Sorted by strand
	os.system("tail -n +8 ./Genomes/{0}.gff | head -n -1 | sort -t \"\t\" -k7,7 -k4,4n > ./Genomes/byStrand.gff".format(genome))
	# Remove previous file if there's any
	os.system('rm ./Genomes/{0}_sorted.gff > /dev/null 2>&1'.format(genome))
	# Sorted by ascending start position on strand +
	os.system("awk '$7 == \"+\"' ./Genomes/byStrand.gff | sort -k4,4n >> ./Genomes/{0}_sorted.gff".format(genome))
	# Sorted by descending start position on strand -
	os.system("awk '$7 == \"-\"' ./Genomes/byStrand.gff | sort -k5,5nr >> ./Genomes/{0}_sorted.gff".format(genome))

	''' Create multiple fasta file of propable aptamer regions '''
	new_sd2.getFasta(
		"-gff", "./Genomes/{0}_sorted.gff".format(sys.argv[1]), 
		"-fasta", "./Genomes/{0}.fasta".format(genome), 
		"-before", 500, 
		"-after", 200, 
		"-aptamer", 50, 
		"-biotype", "protein_coding", 
		"-exhead", True, 
		"-intervals", True)
	
	for i in range(0, len(lista)):
		
		family_id = lista[i].split('.')[0]
		os.system("./Programs/cmsearch --toponly -o ./Results/processing_{1}_{2}.txt ./Alignments/{0} ./aptamer_windows.fasta".format(lista[i], genome, family_id))
		processingfile = open("./Results/processing_{1}_{2}.txt".format(lista[i], genome, family_id), "r")	
		start_scanning = False
		d = {}

		for line in processingfile:
			temp = line.strip().split()
			
			if len(temp) == 0:
				continue

			if temp[0].startswith('>>'):
					start_scanning = True
					continue

			if start_scanning == False:
				if len(temp) > 5 and temp[5].startswith("BSU") and temp[12] == "-":	
					''' Filter outputed aptamers '''
					# E-value
					apt_e_value = float(temp[2])
					if apt_e_value >= e_value:
						continue

					# Prepare data #
					d[temp[0]] = {
							'locus_tag': 			temp[5].split('|')[0],
							'aptamer_start': 		int(temp[6]),
							'aptamer_end': 			int(temp[7]),
							'before_interval': 		int(temp[5].split('|')[1]),
							'score': 				float(temp[3]),
							'gene': {
								'start': 		int(temp[5].split('|')[3]),
								'end': 			int(temp[5].split('|')[4]),
								'strand': 		temp[5].split('|')[5],
							}
						}

			elif start_scanning == True:# and len(temp) >= 12:
				if temp[0] in d and temp[8] == '[]': # If aptamer covers whole model
					key = temp[0]

					if d[key]['gene']['strand'] == '+':
						before_pos = d[key]['gene']['start'] - d[key]['before_interval']
						start = before_pos + d[key]['aptamer_start'] - 1 # -1 because counting starts from 1
						end = before_pos + d[key]['aptamer_end'] - 1 # -1 because counting starts from 1

					elif d[key]['gene']['strand'] == '-':
						before_pos = d[key]['gene']['end'] + d[key]['before_interval']
						# Invert start and end
						start = before_pos - d[key]['aptamer_end'] - 1 # -1 because counting starts from 1
						end = before_pos - d[key]['aptamer_start'] - 1 # -1 because counting starts from 1
							
					switch_name = family_id + '_' + str(start)
					finalFile.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(genome, d[key]['locus_tag'], d[key]['gene']['start'], d[key]['gene']['end'], d[key]['gene']['strand'], switch_name, start, end, d[key]['score']))
					
		processingfile.close()

	finalFile.close()
	
	os.system('rm ./Genomes/byStrand.gff')
	os.system('sort -k3,3n ./Results/{0}.result -o ./Results/{0}.sorted'.format(genome))
	os.system('mv ./Results/{0}.sorted ./Results/{0}.result'.format(genome))

	# Pliki, ktore moga sie pozniej przydac #
	#os.system("rm ./aptamer_windows.fasta") # mam tego nie usuwac dla promotorow
	#os.system("rm ./Results/processing.txt") # nie usuwac tych plikow
	#os.system('rm ./Genomes/{0}_sorted.gff'.format(genome))

	makeAptamersBed(genome)


def terminators(genome):

	os.system("awk \'{ if($1 !~ /^#/){print}}\' Genomes/" + genome + ".gff | tail -n +2 > temp.gff")
	os.system("sort -k4,4n temp.gff -o temp.gff")
	os.system('bedtools closest -s -D a -io -iu -a ./Results/{0}.aptamers.bed -b temp.gff > bed_output.txt'.format(genome))
	os.system('rm temp.gff')

	fh1 = open('bed_output.txt')
	fh2 = open('./Results/{0}.ptt'.format(genome), 'w')

	fh2.write('Location\tStrand\tLength\tPID\tGene\tSynonym\tCode\tCOG\tProduct\n\n\n')

	fh1.close()
	fh2.close()

	# CHYBA DZIAŁA #
	'''./Programs/transterm/transterm -p ./Programs/transterm/expterm.dat termin_temp.fasta termin_crd.coords '''

	### Tworzę plik coords z adnotacjami ###

	#os.system("awk \'BEGIN { OFS=\"\\t\"; } { if($1 ~ /^>/) { split(substr($0,2), t, \"|\"); print $0 \"|1\", \"1\", \"2\", substr($0,2); print $0 \"|2\", t[2]+t[3]-1, t[2]+t[3], substr($0,2)} }\' aptamer_windows.fasta > termin_crd.coords")
	os.system("awk \'BEGIN { OFS=\"\\t\"; } { if($1 ~ /^>/) { split(substr($0,2), t, \"|\"); print $0 \"|1\", \"1\", \"2\", substr($0,2); } }\' aptamer_windows.fasta > termin_crd.coords")

	os.system("./Programs/transterm/transterm -p ./Programs/transterm/expterm.dat aptamer_windows.fasta termin_crd.coords 1> output.tt 2> rubbish.txt")

	### WAZNE !!! ###
	#awk \'BEGIN { OFS=\"\\t\"; } { split(substr($0,2), t, \"|\"); split(substr($0,2), h, \" \"); if(t[2]+t[3] != ) { print $0 \"|1\", \"1\", \"2\", substr($0,2); } }

	#os.system("awk \'BEGIN { OFS=\"\\t\"; } { if($1 ~ /^>/) { split(substr($0,2),list,\"|\"); print $0, \"1\", \"2\", split(substr($0,2); } }\' aptamer_windows.fasta > termin_crd.coords")

	### DEBUG LINE ###
	print("DEBUG")
	return
	######

	### Ptt creation ###



	'''location1=''
	location2=''
	strand=''
	length1=''
	length2=''
	pid=''
	gene1=''
	gene2=''
	synonym=''
	product=''

	1. Przechodzę przez plik bed_output.txt
	1.1 Jeśli gen:
		- zczytaj pozycje APTAMERU i GENU
		- zczytaj nić
		- zczytaj długość APTAMERU i GENU
		- zczytać nazwę APTAMERU
		- zczytać nazwę RYBOSWITCHA
		* Jeśli brak nazwy genu to "-"
		* Jeśli jest to ją zczytaj i zczytaj locus tag

	2.
	3.

	for line in fh1:
		temp = line.split('\t')
		print(line)
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

	fh1.close()
	fh2.close()'''

	# Po co są te oddzielne linijki dla aptamerów i genów w pliku PTT?

	#os.system('rm bed_output.txt')
	
	### End ###

	
	### Zamien naglowek na >ID ###
	os.system("awk \'{if(NR==1){print \">"+genome+"\";} else {print;} }\' ./Genomes/"+genome+".fasta > sequence.fasta")

	'''fh1 = open('./Genomes/{0}.fasta'.format(genome))
	fh2 = open('sequence.fasta', 'w')
	for line in fh1:
		if line[0]=='>':
			fh2.write('>{0}\n'.format(genome))
		else:
			fh2.write(line)'''
	### End ###

	os.system('./Programs/transterm/transterm -p ./Programs/transterm/expterm.dat sequence.fasta ./Results/{0}.ptt > output.tt'.format(genome))
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
terminators(sys.argv[1])
#__init__.runShineDalAnalysis(sys.argv[1], True) # If set true, then meme will be runed
#bedtools(sys.argv[1])
#comparison(sys.argv[1])

print('Done ' + str(strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())))
b = datetime.now()
c = b - a
print("{} seconds {} microseconds".format(c.seconds, c.microseconds % c.seconds))


'''
Tabela: aptamery: scory, pozeycje, sekwencje aptamrow
promotory: pozycje, scory,
terminatory: pozycje, scory

DRS0000001
'''
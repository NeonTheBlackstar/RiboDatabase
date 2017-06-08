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

def createAptamersFilter(result_file):
	filter_list = []
	with open(result_file) as result_handle:
		for line in result_handle:
			line = line.strip().split('\t')
			filter_list.append(line[1]) # Append locus tag
	return(filter_list)


def filterWindows(filter_list, window_file, output_file = ""):
	if output_file == "":
		output_file = window_file.split(".")[0]+"_output."+window_file.split(".")[1]
	writeToFile = False
	with open(window_file) as file_handle, open(output_file, 'w') as output_handle:
		for line in file_handle:
			if line.startswith(">"):
				writeToFile = False
				locus_tag = line.strip().split('|')[0][1:]
				if locus_tag in filter_list:
					writeToFile = True

			if writeToFile == True:
				output_handle.write(line)

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
						'terminator_start': 	int(temp[6]),
						'terminator_end': 		int(temp[7]),
						'before_interval': 		int(temp[5].split('|')[1]),
						'score': 				0,
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

	aptamer_list = createAptamersFilter("./Results/{0}.result".format(genome))
	filterWindows(aptamer_list, "aptamer_windows.fasta", "terminator_windows.fasta")

	os.system("awk \'BEGIN { OFS=\"\\t\"; } { if($1 ~ /^>/) { split(substr($0,2), t, \"|\"); print $0 \"|1\", \"1\", \"2\", substr($0,2); print $0 \"|2\", t[2]+t[3]-1, t[2]+t[3], substr($0,2)} }\' terminator_windows.fasta > termin_crd.coords")
	os.system("./Programs/transterm/transterm -p ./Programs/transterm/expterm.dat terminator_windows.fasta termin_crd.coords 1> transterm_output.tt 2> rubbish.txt")

	scanForTerms = False
	with open("transterm_output.tt") as tt_handle:
		for line in tt_handle:
			line = line.strip()
			if line.startswith("SEQUENCE"):
				header_list = line.split(" ")[1].split("|")
				scanForTerms = True

				# Prepare data #
				d[header_list[0]] = {
					'locus_tag': 			header_list[0],
					'aptamer_start': 		0,
					'aptamer_end': 			0,
					'before_interval': 		header_list[1],
					'score': 				0,
					'gene': {
						'start': 		header_list[3],
						'end': 			header_list[4],
						'strand': 		header_list[5],
					}
				}
			elif scanForTerms == True:
				if line.startswith("TERM"):
					pass

	### DEBUG LINE ###
	print("DEBUG")
	return
	######


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
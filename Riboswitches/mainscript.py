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
### HOW TO USE ###
# python3 mainscript.py NC_000964.3
# python3 mainscript.py all

### HELPER FUNCTIONS ###

def makeAptamersBed(genome):
	os.system("awk \'BEGIN {OFS = \"\\t\"}; {print \"chr\", $7, $8, $2, $9, $5}\' ./Results/"+genome+".result.csv > ./Results/apt.bed")


def makePromotersBed(genome):
	os.system("awk \'BEGIN {OFS = \"\\t\"}; {print \"chr\", $11, $12, $2, 0, $5}\' ./Results/"+genome+".result.csv > ./Results/prom.bed")


def createAptamersFilter(result_file):
	filter_list = []
	with open(result_file) as result_handle:
		for line in result_handle:
			line = line.strip().split('\t')
			filter_list.append(line[5])
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


def intervalIntersect(a1, b1, a2, b2):
	return (a2 < b1) and (b2 > a1)

### END ###

def aptamers(
	genome,				# Genome ID
	e_value = 0.001, 		# Maximum e-value for aptamer score
	):

	# Gather build id for taxonomy, before GFF header will be wiped out #
	genome_build_id = ""
	genome_accession = ""
	# Gather genome info #
	with open("./Genomes/{0}.gff".format(genome)) as handle:
		for line in handle:
			line = line.strip()
			if line.startswith("#!genome-build-accession"):
				genome_accession = line.split()[1].split(":")[1]
				break
			elif line.startswith("#!genome-build"):
				genome_build_id = line.split(" ")[1]

	''' Prepare separate files for all replicons '''
	# GFF #
	with open("./Genomes/{0}.gff".format(genome)) as handle:
		#replicon_id = ""
		counter = 0
		replicon_handle = None

		for line in handle:
			if line.startswith("##sequence-region"):
				counter += 1
				if replicon_handle != None:
					replicon_handle.close()
				replicon_handle = open("./Genomes/{0}-replicon-{1}.gff".format(genome, counter), "w")

			elif not line.startswith("#"):
				replicon_handle.write(line)
		replicon_handle.close()

	# FASTA #
	with open("./Genomes/{0}.fasta".format(genome)) as handle:
		counter = 0
		replicon_handle = None

		for line in handle:
			if line.startswith(">"):
				counter += 1
				if replicon_handle != None:
					replicon_handle.close()
				replicon_handle = open("./Genomes/{0}-replicon-{1}.fasta".format(genome, counter), "w")

			replicon_handle.write(line)
		replicon_handle.close()

	replicon_files = [ file for file in os.listdir('Genomes') if "replicon" in file and file.endswith("gff") and genome in file ]

	os.system("touch temp.fasta")
	for file in replicon_files:
		counter = file.split("-")[-1].split(".")[0]
		# Sorted by strand
		os.system("sort -t \"\t\" -k7,7 -k4,4n ./Genomes/{0} > ./Genomes/byStrand_{1}.gff".format(file, counter))
		# Remove previous file if there's any
		os.system('rm ./Genomes/{0}_sorted_{1}.gff > /dev/null 2>&1'.format(genome, counter))
		# Sorted by ascending start position on strand +
		os.system("awk '$7 == \"+\"' ./Genomes/byStrand_{1}.gff | sort -k4,4n >> ./Genomes/{0}_sorted_{1}.gff".format(genome, counter))
		# Sorted by descending start position on strand -
		os.system("awk '$7 == \"-\"' ./Genomes/byStrand_{1}.gff | sort -k5,5nr >> ./Genomes/{0}_sorted_{1}.gff".format(genome, counter))

		organism_info = new_sd2.getFasta(
			"-gff", "./Genomes/{0}_sorted_{1}.gff".format(genome, counter), 
			"-fasta", "./Genomes/{0}-replicon-{1}.fasta".format(genome, counter), 
			"-before", 500, 
			"-after", 200, 
			"-aptamer", 50, 
			"-biotype", "protein_coding",
			"-exhead", True, 
			"-intervals", True,
			)

		os.system("cat aptamer_windows.fasta >> temp.fasta")
	
	os.system("mv temp.fasta aptamer_windows.fasta")

	################################################

	finalFile = open("./Results/{0}.result.csv".format(genome), "w")

	# Add general and aptamer headers
	finalFile.write(
		"organism_accession_number\t"+
		#"scientific_name\t"+
		"build_id\t"+
		###
		"taxonomy_id\t"+
		"gene_name\t"+
		"location\t"+
		"locus_tag\t"+
		"gene_start\t"+
		"gene_end\t"+
		"strand\t"+
		"class_name\t"+
		"class_description\t"+
		"aptamer?name\t"+
		"aptamer_start\t"+
		"aptamer_end\t"+
		"aptamer_score\t"+
		"replicon_id\t"+
		"sequence\t"+
		"\n")
	
	riboswitchCount = 0

	lista = os.listdir('Alignments')
	for i in range(0, len(lista)):

		# Read aptamer class info for the result file #
		class_name = ""
		class_desc = ""
		with open("./Alignments/{0}".format(lista[i])) as class_handle:
			for line in class_handle:
				line = line.strip()
				if line.startswith("NAME"):
					class_name = line.split()[1]
				elif line.startswith("DESC"):
					class_desc = " ".join(line.split()[1:])
					break
		# End #
		
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
				if len(temp) > 5 and len(temp) < 16 and temp[0].startswith("(") and temp[12] == "-":
				
					''' Filter outputed aptamers '''
					# E-value
					apt_e_value = float(temp[2])
					if apt_e_value >= e_value:
						continue

					### Prepare data ###
					d[temp[0]] = {
						'locus_tag': 			temp[5].split('|')[0],
						'aptamer_start': 		int(temp[6]),
						'aptamer_end': 			int(temp[7]),
						'before_interval': 		int(temp[5].split('|')[1]),
						'score': 				float(apt_e_value), # !!!
						'gene': {
							'locus_tag': 	temp[5].split('|')[0],
							'start': 		int(temp[5].split('|')[3]),
							'end': 			int(temp[5].split('|')[4]),
							'strand': 		temp[5].split('|')[5],
							'name':			temp[5].split('|')[6],
							'location':		temp[5].split('|')[7],
							'replicon_id':	temp[5].split('|')[8],
						}
					}

					# Get sequence from FASTA file #
					getSeq = False
					windowSequence = ""
					with open("./aptamer_windows.fasta") as apt_handle:
						for l in apt_handle:
							if l.startswith(">"):
								if d[temp[0]]['gene']['locus_tag'] in l:
									getSeq = True
								else:
									if getSeq == True:
										break
							else:
								if getSeq == True:
									windowSequence += l.strip()

					d[temp[0]]['gene']['sequence'] = windowSequence
					### END ###

			elif start_scanning == True:
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
					finalFile.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
						genome_accession, 
						genome_build_id,
						organism_info['tax'], 
						d[key]['gene']['name'], 
						d[key]['gene']['location'], 
						d[key]['gene']['locus_tag'], 
						d[key]['gene']['start'], 
						d[key]['gene']['end'], 
						d[key]['gene']['strand'],
						class_name,
						class_desc,
						switch_name, 
						start, 
						end, 
						d[key]['score'],
						d[key]['gene']['replicon_id'],
						windowSequence))

					riboswitchCount += 1

		processingfile.close()

	finalFile.close()

	os.system('rm ./Genomes/byStrand*.gff')
	os.system("rm ./Results/processing*.txt")
	os.system('rm ./Genomes/{0}_sorted*.gff'.format(genome))
	os.system('rm ./Genomes/{0}-replicon*.fasta'.format(genome))
	os.system('rm ./Genomes/{0}-replicon*.gff'.format(genome))

	# Posortuj plik wynikowy
	os.system('head -n 1 ./Results/{0}.result.csv > ./Results/{0}_temp.result.csv'.format(genome))
	os.system('tail -n +2 ./Results/{0}.result.csv | sort -k7,7n >> ./Results/{0}_temp.result.csv'.format(genome))
	os.system('mv ./Results/{0}_temp.result.csv ./Results/{0}.result.csv'.format(genome))

	#makeAptamersBed(genome)
	return(riboswitchCount)


def terminators(genome):

	aptamer_list = createAptamersFilter("./Results/{0}.result.csv".format(genome))
	filterWindows(aptamer_list, "aptamer_windows.fasta", "terminator_windows.fasta")

	# Generowanie pliku .coords dla Transterma # 
	os.system("awk \'BEGIN { OFS=\"\\t\"; } { if($1 ~ /^>/) { split(substr($0,2), t, \"|\"); print \"gene1\", \"1\", \"2\", substr($0,2); print \"gene2\", t[2]+t[3]-1, t[2]+t[3], substr($0,2)} }\' terminator_windows.fasta > termin_crd.coords")
	os.system("./Programs/transterm/transterm -p ./Programs/transterm/expterm.dat terminator_windows.fasta termin_crd.coords 1> transterm_output.tt 2> errors.txt")

	d = {}
	with open("transterm_output.tt") as tt_handle, open("./Results/{}.result.csv".format(genome),"r") as result_handle:
		for line in tt_handle:
			line = line.strip()
			if line.startswith("SEQUENCE"):
				header_list = line.split(" ")[1].split("|")
				locus_tag = header_list[0]

				d[locus_tag] = {
					'gene': {
						'locus_tag': 	locus_tag,
						'start': 		int(header_list[3]),
						'end': 			int(header_list[4]),
						'strand': 		header_list[5],
						'before': 		int(header_list[1]),
					},
					'terminators': [],
				}

			elif line.startswith("TERM"):
				# Zebranie danych #
				term_list = line.split()

				if d[locus_tag]['gene']['strand'] == '+':
					before_pos = d[locus_tag]['gene']['start'] - d[locus_tag]['gene']['before']
					terminator_start = 	before_pos + int(term_list[2]) - 1
					terminator_end = 	before_pos + int(term_list[4]) - 1

				elif d[locus_tag]['gene']['strand'] == '-':
					before_pos = d[locus_tag]['gene']['end'] + d[locus_tag]['gene']['before']
					terminator_start = 	before_pos - int(term_list[4]) - 1
					terminator_end = 	before_pos - int(term_list[2]) - 1

				terminator = {
					'start': 			terminator_start,
					'end': 				terminator_end,
					'confidence': 				int(term_list[7]),
					'harpin_score':		float(term_list[8]),
					'tail_score':		float(term_list[9]),
				}

				d[locus_tag]['terminators'].append(terminator.copy())

		# Choosing the best, not overlapping terminator and removing the rest of them
		firstLine = True				
		for line in result_handle:
			line = line.strip()

			if firstLine:	# Ommit first line with headers
				firstLine = False
				continue

			line_list = line.strip().split('\t')
			locus_tag = line_list[5]
			strand = line_list[8]
			aptamer_start = int(line_list[12])
			aptamer_end = int(line_list[13])
			terms_copy = list(d[locus_tag]['terminators'])

			for id1 in range(0,len(terms_copy)):
				for id2 in range(id1 + 1,len(terms_copy)):
					t1 = terms_copy[id1]
					t2 = terms_copy[id2]

					# If terminators overlap with each other
					if intervalIntersect(t1['start'], t1['end'], t2['start'], t2['end']) == True:
								
						# I leave terminator with better confidence
						if t1['confidence'] < t2['confidence']:
							if t1 in d[locus_tag]['terminators']:
								d[locus_tag]['terminators'].remove(t1)
						elif t1['confidence'] > t2['confidence']:
							if t2 in d[locus_tag]['terminators']:
								d[locus_tag]['terminators'].remove(t2)
						# If the same score, I leave the one with bigger energy difference between harping and poli-T
						else:
							t1_score_difference = abs(t1['harpin_score'] - t1['tail_score'])
							t2_score_difference = abs(t2['harpin_score'] - t2['tail_score'])

							if t1_score_difference <= t2_score_difference:
								if t1 in d[locus_tag]['terminators']:
									d[locus_tag]['terminators'].remove(t1)
							else:
								if t2 in d[locus_tag]['terminators']:
									d[locus_tag]['terminators'].remove(t2)
					# If not overlapping
					else:
						try:
							# Calculate distance from aptamer
							t1_length = abs(t1['start'] - t1['end'])
							t2_length = abs(t2['start'] - t2['end'])
							if strand == "+":
								t1_distance = t1['start'] - aptamer_end
								t2_distance = t2['start'] - aptamer_end
							if strand == "-":
								t1_distance = aptamer_start - t1['end']
								t2_distance = aptamer_start - t2['end']

							# When none of terminators overlap with aptamer
							if t1_distance >= 0 and t2_distance >= 0:
								if t1_distance < t2_distance:
									if t2 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t2)
								else:
									if t1 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t1)

							# If distance is negative, it means that terminator overlaps aptamer
							elif t1_distance < 0 and t2_distance >= 0:
								if abs(t1_distance) < (t1_length / 2):
									if t2 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t2)
								else:
									if t1 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t1) 

							elif t1_distance >= 0 and t2_distance < 0:
								if abs(t2_distance) < (t2_length / 2):
									if t1 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t1)
								else:
									if t2 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t2)

							elif t1_distance < 0 and t2_distance < 0:
								if abs(t1_distance) < (t1_length / 2):
									if t2 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t2)
								elif abs(t2_distance) < (t2_length / 2):
									if t1 in d[locus_tag]['terminators']:
										d[locus_tag]['terminators'].remove(t1)
								else:
									if abs(t1_distance) < abs(t2_distance):
										if t2 in d[locus_tag]['terminators']:
											d[locus_tag]['terminators'].remove(t2)
									else:
										if t1 in d[locus_tag]['terminators']:
											d[locus_tag]['terminators'].remove(t1)
						except ValueError:
							continue

		# Zapis do pliku
		firstLine = True
		result_handle.seek(0)
		with open("./Results/{}_temp.result.csv".format(genome),"w") as temp_result:
			for line in result_handle:
				line = line.strip()

				if firstLine:	# Ommit first line with headers
					firstLine = False
					line += "\t" + "terminator_start" + "\t" + "terminator_end" + "\t" + "terminator_score" + "\n"
				else:
					line_list = line.strip().split('\t')
					locus_tag = line_list[5]

					if d[locus_tag]['terminators'] != []: # If terminator for that aptamer was found
						line += "\t" + str(d[locus_tag]['terminators'][0]['start']) + "\t" + str(d[locus_tag]['terminators'][0]['end']) + "\t" + str(d[locus_tag]['terminators'][0]['confidence']) + '\n'
					else:
						line += "\t" + '0' + "\t" + '0' + "\t" + '0' + '\n'			
				temp_result.write(line)

		os.system("mv \"./Results/{0}_temp.result.csv\" \"./Results/{0}.result.csv\"".format(genome))

	os.system('rm aptamer_windows.fasta')
	os.system('rm terminator_windows.fasta')
	os.system('rm errors.txt')
	os.system('rm termin_crd.coords')
	os.system('rm transterm_output.tt')


##### SCRIPT STARSTS HERE #####
'''
os.system('rm ./Genomes/byStrand*.gff')
os.system('rm ./Genomes/{0}_sorted*.gff'.format(sys.argv[1]))
os.system('rm ./Genomes/{0}-replicon*.fasta'.format(sys.argv[1]))
os.system('rm ./Genomes/{0}-replicon*.gff'.format(sys.argv[1]))
'''
if sys.argv[1] == "all":
	os.system("rename 's/\.fna$/\.fasta/' ./Genomes/*.fna > /dev/null 2>&1")
	genomes_list = [ file[:-4] for file in os.listdir('Genomes') if file.endswith(".gff") ]
else:
	genomes_list = [sys.argv[1]]

for genome in genomes_list:
	a = datetime.now()

	switchesFound = aptamers(genome)
	terminators(genome)

	b = datetime.now()
	c = b - a

	print("{}\t{}MB\t{}MB\t{}s\t{}".format(
		genome,
		round(os.path.getsize("./Genomes/"+genome+".fasta")/10**6, 2), 
		round(os.path.getsize("./Genomes/"+genome+".gff")/10**6, 2),
		round(c.seconds + c.microseconds / 1000000, 1),
		switchesFound
	))



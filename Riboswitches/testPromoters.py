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
# python3 testPromoters.py bsub_all_genes.txt bsub NC_000964.3
## DEPARTED # python3 testPromoters.py all GCF_000005845.2_ASM584v2_genomic
## DEPARTED # python3 testPromoters.py NC_000964.3 GCF_000005845.2_ASM584v2_genomic

def tableConverter(
	fileToConvert = sys.argv[1],
	organism = sys.argv[2]
	):

	outputFile = fileToConvert.split('.')[0]+"_converted.txt"
	with open(fileToConvert) as handle, open(outputFile, 'w') as out:
		next(handle)
		
		for line in handle:
			_list = line.split('\t')

			if organism == "bsub":
				if not (_list[1] != "\"\"" and ":EV-EXP" not in _list[2]):
					out.write("{}\t{}\n".format(_list[0], _list[1]))
			elif organism == "ecoli":
				if _list[0] != "" and not (_list[1] != "\"\"" and ":EV-EXP" not in _list[2]):
					out.write("{}\t{}\n".format(_list[0][1:-1], _list[1]))
	return outputFile


def test_promoters( # Test dla Bacillusa
	genome_id = sys.argv[3:], 									# Genome ID
	genome_fasta = ['./Genomes/{}.fasta'.format(genome) for genome in sys.argv[3:]],	# Genome fasta file path
	window = '100', 											# Window size for the upstream region to be compared
	gccontent = 'default',										# GC-content of the whole genome
	programs = [],
	tablesToLoad = ["ecoli_all_genes_converted.txt"]
	):
	
	#aptamer_list = createAptamersFilter("./Results/{0}.result.csv".format(genome))
	#filterWindows(aptamer_list, "aptamer_windows.fasta", "promoter_windows.fasta")

	#tablesToLoad = ["bsub_all_genes_converted.txt", "ecoli_all_genes_converted.txt"]
	for id, genome in enumerate(genome_id):
		print("Testing {}...\n".format(genome))

		### PREPARE TESTING DICTIONARY ###
		roca_dictionary = {}	# Dictionary of locus tags as keys and presence of prom as value
		promList = [] 	# List of locus tags
		with open(tablesToLoad[id]) as conf_h:
			for line in conf_h:
				line = line.strip().split('\t')
				roca_dictionary[line[0]] = {
						'confirmed': True if line[1] != "\"\"" else False,
						'bprom': False,
						'ppred': False,
						'btss': False,
						}
		promList = list(roca_dictionary)
	
		# Sorted by strand
		os.system("sort -t \"\t\" -k7,7 -k4,4n ./Genomes/{0}.gff > ./Genomes/byStrand.gff".format(genome))
		# Remove previous file if there's any
		os.system('rm ./Genomes/{0}_sorted.gff > /dev/null 2>&1'.format(genome))
		# Sorted by ascending start position on strand +
		os.system("awk '$7 == \"+\"' ./Genomes/byStrand.gff | sort -k4,4n >> ./Genomes/{0}_sorted.gff".format(genome))
		# Sorted by descending start position on strand -
		os.system("awk '$7 == \"-\"' ./Genomes/byStrand.gff | sort -k5,5nr >> ./Genomes/{0}_sorted.gff".format(genome))

		new_sd2.getFasta(
			"-gff", "./Genomes/{0}_sorted.gff".format(genome), 
			"-fasta", "./Genomes/{0}.fasta".format(genome), 
			"-before", 500, 
			"-after", 200, 
			"-aptamer", 50, 
			"-biotype", "protein_coding",
			"-exhead", True, 
			"-intervals", True,
			"-filterPR", promList,
			)

		# Remove from filter genes which were not found in annotation file
		for locusTag in promList:
			del roca_dictionary[locusTag]

		os.system("mv aptamer_windows.fasta promoter_windows.fasta")
		os.system('rm ./Genomes/byStrand.gff')
		os.system('rm ./Genomes/{0}_sorted.gff'.format(genome))


		if "prompredict" in programs:
			######### RUN PROMPREDICT #########
			gccontent = float(subprocess.check_output("./Programs/gc_calc Genomes/{0}.fasta".format(genome), shell=True))
			os.system('echo \'{0}\n{1}\n{2}\' | ./Programs/PromPredict_mulseq'.format("promoter_windows.fasta", window, gccontent))

			PP_output_path = glob('./*_PPde.txt')[0]
			
			
			### COLLECT DATA FOR ROC FROM PROMPREDICT ###
			with open(PP_output_path) as PPout:
				for line in PPout:
					line = line.strip().split('\t')
					if line[0] == 'ID':
						ID_line = line[1].split('|')
						gene_name = ID_line[0]
						roca_dictionary[gene_name]['ppred'] = False
					elif line[0].startswith('>'):
						roca_dictionary[gene_name]['ppred'] = True


			### COUNT PROM PROMPREDICT HITS ###
			true_positive = 0
			true_negative = 0
			false_negative = 0
			false_positive = 0

			for g in roca_dictionary:
				g = roca_dictionary[g]
				if g['confirmed'] == True and g['ppred'] == True:
					true_positive += 1
				elif g['confirmed'] == False and g['ppred'] == False:
					true_negative += 1
				elif g['confirmed'] == True and g['ppred'] == False:
					false_negative += 1
				else:
					false_positive += 1

			print("#PP# Czulosc: {}%, swoistosc: {}%".format( (true_positive/(true_positive + false_negative))*100, (true_negative/(true_negative+false_positive))*100 ))

			### Clean up ###
			os.system('rm ./*_PPde.txt')
			os.system('rm ./*_stb.txt')
			os.system('rm ./*_GCstat.txt')


		if "bprom" in programs:
			############# BPROM ################ ma ograniczenie co do wielkości fasta. Nie pójdzie na całym genomie. W przypadku multifasta bierze tylko pierwszy header i dalej nie idzie!
			os.system('export TSS_DATA="./Programs/lin/data > /dev/null 2>&1"')
			os.system('rm -r bprom')

			counter = 1
			temp_window = ''

			if not os.path.exists("./bprom"):
				os.makedirs("./bprom")

			with open('./promoter_windows.fasta') as prom_windows:
				for line in prom_windows:
					if line.startswith('>'):
						if temp_window != '':
							with open('./temp_prom.fasta', 'w') as temp_prom:
								temp_prom.write(temp_window)
								temp_window = ''
							os.system('Programs/lin/bprom \"{0}\" \"bprom/output_{1}.txt\"'.format("./temp_prom.fasta", counter))
							counter += 1
					temp_window += line
				else:
					with open('./temp_prom.fasta', 'w') as temp_prom:
						temp_prom.write(temp_window)
					os.system('Programs/lin/bprom \"{0}\" \"bprom/output_{1}.txt\"'.format("./temp_prom.fasta", counter))

				prom_windows.close()

			### COLLECT DATA FOR ROC FOR BPROM ###
			for file in os.listdir('./bprom'):
				if file.startswith('output'):
					with open('./bprom/{}'.format(file)) as file_h:
						gene_name = ''
						locus_tag = ''
						promoterExists = False

						for line in file_h:
							line = line.strip()
							if line.startswith('>'):
								locus_tag = line.split('|')[0][1:]
								continue

							if line.startswith('Number'): 
								if int( line.split('-')[1].strip() ) > 0:
									roca_dictionary[locus_tag]['bprom'] = True
								else:
									roca_dictionary[locus_tag]['bprom'] = False
								break

			############# BPROM END ################
			true_positive = 0
			true_negative = 0
			false_negative = 0
			false_positive = 0

			for g in roca_dictionary:
				g = roca_dictionary[g]
				if g['confirmed'] == True and g['bprom'] == True:
					true_positive += 1
				elif g['confirmed'] == False and g['bprom'] == False:
					true_negative += 1
				elif g['confirmed'] == True and g['bprom'] == False:
					false_negative += 1
				else:
					false_positive += 1

			print("#BPROM# Czulosc: {}%, swoistosc: {}%".format( (true_positive/(true_positive + false_negative))*100, (true_negative/(true_negative+false_positive))*100 ))

			### Clean up ###
			os.system('rm -r ./bprom/')
			os.system('rm temp_prom.fasta')


		if "btssfinder" in programs:

			nuc_content = ",".join(subprocess.check_output("./Programs/atgc_freqs Genomes/{0}.fasta".format(genome), shell=True).decode('UTF-8').split('\t'))

			os.system('export bTSSfinder_Data=./Programs/BTSSFINDER/Data')
			#os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS -h 1 -t e -c 1')
			'''a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS70 -h 1 -t e -c 70 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("sigma70: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))

			a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS38 -h 1 -t e -c 38 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("sigma38: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))

			a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS32 -h 1 -t e -c 32 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("sigma32: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))

			a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS28 -h 1 -t e -c 28 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("sigma28: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))

			a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSS24 -h 1 -t e -c 24 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("sigma24: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))'''

			a = datetime.now()
			os.system('Programs/BTSSFINDER/bTSSfinder -i promoter_windows.fasta -o testbTSSall -h 1 -t e -c 1 -n {}'.format(nuc_content))
			b = datetime.now()
			c = b - a
			print("All: {}".format(round(c.seconds + c.microseconds / 1000000, 1)))

			print("bTSSfinder")

			tssresult_list = [ file for file in os.listdir('.') if file.endswith(".bed") and file.startswith("testbTSS") ]

			for r in tssresult_list:
				with open(r) as r_handle:
					for line in r_handle:
						gene_tag = line.split("|")[0]
						roca_dictionary[gene_tag]['btss'] = True

				true_positive = 0
				true_negative = 0
				false_negative = 0
				false_positive = 0

				for g in roca_dictionary:
					g = roca_dictionary[g]
					if g['confirmed'] == True and g['btss'] == True:
						true_positive += 1
					elif g['confirmed'] == False and g['btss'] == False:
						true_negative += 1
					elif g['confirmed'] == True and g['btss'] == False:
						false_negative += 1
					else:
						false_positive += 1

					g['btss'] = False

				print("#BTSSFINDER: {}# Czulosc: {}%, swoistosc: {}%".format( r, (true_positive/(true_positive + false_negative))*100, (true_negative/(true_negative+false_positive))*100 ))

				### Clean up ###
				os.system('rm ./testbTSS*.*')


	### Clean up everything ###
	os.system('rm promoter_windows.fasta')

	#print("debug") ### TU SKONCZYLEM
	#exit(1)


##### SCRIPT STARSTS HERE #####

convertedFile = tableConverter()
#test_promoters(programs = ["prompredict","bprom", "btssfinder"], tablesToLoad = [convertedFile])
test_promoters(programs = [], tablesToLoad = [convertedFile])
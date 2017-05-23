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
#	argparse - do interfejsu programów terminalowych

# python3 mainscript.py NC_000964.3

# Sprawdzic czy ktorys program wymaga instalacji TYLKO DO SD

# Między window a results jest przesunięcie o 1 nukleotyd! Ogarnąć!

# Struktura drugorzedowa aptamerow w pliku proccessing?

# Zapisywać pliki proccessing, przydzaza sie do przewidywania struktury ZROBIONE

# Filtrować po e-value granica: 0.001, i po pokryciu modelu: [] jest dopasowany kompletnie, .. jest niedopasowany calkowcie po obu stronach, ~] tylko po jednej stronie ZROBIONE

# Zapisywac do pliku score czy e-value? E-value

# Napisac programik do liczenia GC w C++/ANSI C (moze bedzie szybszy?)

# Porównać działanie PromPredicta z BPromem!
# Dać ramkę jak w aptamerach dla promotorów
# Podawać te okna pojedynczo - pliki w RAMie? JEST PROMPREDICT MULTISEQ!

# Dla dokladnie tych samych ramek co aptamery? (przekaznik -apt)

'''
Znalezc publikacje z doswiadczalnie potwierdzonymi miejscai startu transkrycji, promotorami TRUE POSITIVES
Potem poszukać genów operonowych, które wiemy, ze nie maja promotorow FALSE POSITIVES
Wyekstrahowac ramki poszukiwania dla tych genow i sprawdzic specyficznosc i dzialanie 

RocR - pakiet R - do okreslacia specyficznosci i czulosci dzialania programu, poczytac sobie o krzywej Roca

Poczytac sobie publikacje
https://academic.oup.com/bioinformatics/article-lookup/doi/10.1093/bioinformatics/btq577


########################################################################################################################################################################################


ogarnac jak wyznaczyc ten relaiability level na podstawie wyników z Prompredicta multiseq !

|lsp|	|lspe|	|Dmax pos|	|Dmax|	|Dave|{Average DE value for Predicted Promoter}

DE to "relative stability between neighboring regions of 100 nt length with respect to every nucleotide position n"
DE to "difference in free energy, czyli E1 - E2"

Dave to PRAWDOPODOBNIE PP_DEave, czyli średnia wartość DE dla każdego przewidzianego promotora
Sigma?
Mikro?

AFE to E1, czyli suma energii swobodnych nukleotydów od N do N+100 podzielona przez 100

‘REav’, the AFE values calculated over the +100 to +500 nt regions downstream of the TSSs and TLSs

E i D znamy, to wartości cutoffów dobrane dla poszczególnych cutoffów GC%

The average free energy (AFE)

gene translation start sites (TLSs)


The values of E the AFE over −80 to +20 region and REav which is the AFE over the +100 to +500 region with respect to TLS are also shown for all %GC classes which have more than 100 sequences.
D = E −REav

ujemna wartosc to na pewno bedzie jakas energia swobodna

TSS-based dataset (i.e. experimentally identified transcription start sites) 

The average DE values for all predicted regions in a particular genome have also been calculated and denoted as WPP_DEave (μ)

(σ = 8.3) recall value
An average recall value of 72% (which indicates the percentage of protein and RNA coding genes with predicted promoter regions assigned to them)

On an average, 86.4% (σ = 5.3) of DNA is transcribed as protein or RNA


!!!

$11 D ave
$12 Reliability
tail -n +4 _PPde.txt | sort -k11 | awk '{print $11, $12}' > prom_score.temp

!!!

"Since no correlation was observed for PP_DEave based on %GC, in the current study we have chosen this as an unbiased parameter to define the reliability level for each prediction within whole genome."

'''
'''
Filtrowanie bedzie do parametrze Dave.
Napisać do tych gości i spytać się, co dokładnie oznaczają wszystkie parametry w pliku wynikowym _PPde, czy i jak można określić pozycję startu miejsca transkrypcji (TATA BOX), oraz czy dobrze rozumiem, jak to jest obliczane. Można spytać również o te "Supplementary data".

lsp - least stable position	
lspe - least stable position energy

### 10.05.17 ###

Szukalem tych promotorow, ale wszystkie linki powygasaly, bo ostatni update tej bazy danych z Bacillusa jest z 2008 r... ;/

To jest dla E. coli i wygląda całkiem spoko:
http://regulondb.ccg.unam.mx/index.jsp

Tutaj publikacje o tej bazie DBTBS, gdzie niby mialy by byc prmotory dla Bacillusa sub.:
https://academic.oup.com/nar/article/29/1/278/1116240/DBTBS-a-database-of-Bacillus-subtilis-promoters
https://www.ncbi.nlm.nih.gov/pubmed/14681362

Sama strona DBTBS:
http://dbtbs.hgc.jp/

Tu niby cos jest, ale strasznie malo tych promotorow, bo tylko 20:
http://microbes.ucsc.edu/cgi-bin/hgTables?hgsid=2707680_eeRoFcyRayQVESRA1SG6pYG48ah0&clade=bacteria-firmicutes&org=Bacillus+subtilis&db=baciSubt2&hgta_group=allTracks&hgta_track=ct_Promoter_7933&hgta_table=0&hgta_regionType=genome&position=chr%3A10001-35000&hgta_outputType=wigData&hgta_outFileName=

############### 17.05.17 ################

Nie potrafię zrozumieć notacji nazw genów w tym BioCycu. Nazwa często nie wskazuje na to, że jest to gen pojedynczy, czy jest to oznaczenie operonu.

############### 22.05.17 ################

Zrobić terminatory na tych samych oknach co aptamery też od kodonu START. Terminator powinien być pomiędzy kodonem START a aptamerem, może lekko nachodzić na aptamer.
Ogarnąć ręczną analizę tych promotorów.
Czy PromPredict robię tę analizę z uwzględnieniem nici ujemnej? Bo tak to nie wygląda...

'''
'''_______________________________________________________________________'''

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

'''
Szukamy na tych samych oknach co aptamery, zeby dwa razy tego nie ekstrahowac.
Jesli promotor zostanie znaleziony przed pozycją aptameru, to dodajemy go do wyniku.
'''
def promoters(
	genome_id = sys.argv[1], 									# Genome ID
	genome_fasta = './Genomes/{}.fasta'.format(sys.argv[1]),	# Genome fasta file path
	window = '100', 											# Window size for the upstream region to be compared
	gccontent = 'default'										# GC-content of the whole genome
	):
	
	# GC content dla ramki, czy dla calego genomu? DLA CALEGO GENOMU
	# Zwiększyć okno "window" do 500, skoro taka jest ramka dla aptameru? TAKA SAMA RAMKA JAK DLA APTAMERU
	# Robić filtrowanie dla znalezionych promotorów? OGARNĄĆ JAK OBLICZYĆ TE LEVELE

	gccontent = float(subprocess.check_output("./Programs/gc_calc Genomes/{0}.fasta".format(genome_id), shell=True))
	# Create filter with genes, around which an aptamer was found
	filter_list = createPromoterFilter("./Results/{0}.result".format(genome_id))
	# Generate multifasta file with windows for promoters search
	new_sd2.getFasta(
		"-gff", "./Genomes/{0}_sorted.gff".format(genome_id), 
		"-fasta", "./Genomes/{0}.fasta".format(genome_id), 
		"-before", 500, 
		"-after", 200, 
		"-biotype", "protein_coding", 
		"-exhead", True, 
		"-filterPR", filter_list,
		"-intervals", True,
		"-genename", True)

	### Use PromPredictMultiseq to find promoters in multifasta file ###
	#os.system('echo \'{0}\n{1}\n{2}\' | ./Programs/PromPredict_mulseq'.format("promoter_windows.fasta", window, gccontent)) 
	#os.system('echo \'{0}\n{1}\n{2}\' | ./Programs/PromPredict_genome_V1'.format(genome_fasta, window, gccontent)) 

	############# LOAD ALL GENES ##############
	'''
	roca_dictionary = {}

	handle = open('./Genomes/{}.gff'.format(genome_id))

	for record in GFF.parse(handle):
		for feature in record.features:
			if feature.type == 'gene' and (feature.qualifiers['gene_biotype'][0] == 'protein_coding'):
				roca_dictionary[ feature.qualifiers['gene'][0] ] = {
					'confirmed': False,
					'bprom': False,
					'ppred': False,
				}
	'''
	############# LOAD CONFIRMED PROMOTERS ############## confirmed_promoters.txt
	'''
	with open('confirmed_promoters.txt') as conf_h:
		for line in conf_h:
			line = line.strip().split('\t')
			
			if line[3] != '':
				gene_name = line[3].split('-')[0]
				roca_dictionary[gene_name]['confirmed'] = True

	print(roca_dictionary)

	print("debug") ### TU SKONCZYLEM
	return
	'''
	############# BPROM ################ ma ograniczenie co do wielkości fasta. Nie pójdzie na całym genomie. W przypadku multifasta bierze tylko pierwszy header i dalej nie idzie!
	'''
	os.system('export TSS_DATA=\"Programs/lin/data\"')

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

	### COLLECT DATA FOR ROC ###

	for file in os.listdir('./bprom'):
		if file.startswith('output'):
			with open('./bprom/{}'.format(file)) as file_h:
				gene_name = ''
				locus_tag = ''
				promoterExists = False

				for line in file_h:
					line = line.strip()
					if line.startswith('>'):
						gene_name = line.split('|')[3]
						locus_tag = line.split('|')[0][1:]
						continue

					if line.startswith('Number'): 
						if int( line.split('-')[1].strip() ) > 0:
							roca_dictionary[gene_name]['bprom'] = True
						else:
							roca_dictionary[gene_name]['bprom'] = False
						break

	print(roca_dictionary)
	'''
	############# BPROM END ################
	### USAGE ###
	# export TSS_DATA="Programs/lin/data"
	# Programs/lin/bprom ./Genomes/NC_000964.3.fasta bprom_output.txt


	############# PROMPREDICT START ################

	PP_output_path = glob('./*_PPde.txt')[0]

	os.system('echo \'{0}\n{1}\n{2}\' | ./Programs/PromPredict_mulseq'.format("promoter_windows.fasta", window, gccontent))
	
	### COLLECT DATA FOR ROC ###
	'''
	with open(PP_output_path) as PPout:
		for line in PPout:
			line = line.strip().split('\t')
			if line[0] == 'ID':
				ID_line = line[1].split('|')
				gene_name = ID_line[3]
				roca_dictionary[gene_name]['ppred'] = False
			elif line[0].startswith('>'):
				roca_dictionary[gene_name]['ppred'] = True

	print(roca_dictionary)
	'''
	############# PROMPREDICT END ################

	PP_output_path = glob('./promoter_windows_PPde.txt')[0]
	ID_line = None
	d = {}

	# Read whole final file #
	finalFile = ""

	with open("./Results/{0}.result".format(genome_id), "r") as handle:
		finalLines = handle.readlines()

	with open("./Results/{0}.result".format(genome_id), 'w') as finalFile, open(PP_output_path) as PPout:
		for line in PPout:
			line = line.strip().split('\t')
			if line[0] == 'ID':
				ID_line = line[1].split('|')
				'''
				d = {
					'locus_tag': ID_line[0],
					'before_interval': int(ID_line[1]),
					'gene': {
						'start': 		int(ID_line[3]),
						'end': 			int(ID_line[4]),
						'strand': 		ID_line[5],
					}
				}
				'''
				d = {
					'locus_tag': ID_line[0],
					'before_interval': int(ID_line[1]),
					'gene': {
						'start': 		int(ID_line[4]),
						'end': 			int(ID_line[5]),
						'strand': 		ID_line[6],
					}
				}

			elif line[0].startswith('>'):
				pos = line[0]
				promoter_start = int(pos[1:].split("..")[0])
				promoter_end = int(pos[1:].split("..")[1])

				if d['gene']['strand'] == '+':
					before_pos = d['gene']['start'] - d['before_interval']
					start = before_pos + promoter_start - 1 # -1 because counting starts from 1
					end = before_pos + promoter_end - 1 # -1 because counting starts from 1

				elif d['gene']['strand'] == '-':
					before_pos = d['gene']['end'] + d['before_interval']
					# Invert start and end
					start = before_pos - promoter_end - 1 # -1 because counting starts from 1
					end = before_pos - promoter_start - 1 # -1 because counting starts from 1

				promoter_name = 'PR_' + str(start)
				for line in finalLines:
					line = line.strip()
					if line.split('\t')[1] == d['locus_tag']:
						finalFile.write("{}\t{}\t{}\t{}\n".format(line, promoter_name, start, end))
						break

	makePromotersBed(genome_id)

	print("debug") ### TU SKONCZYLEM
	return

	# BEDTOOLS

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
promoters()
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
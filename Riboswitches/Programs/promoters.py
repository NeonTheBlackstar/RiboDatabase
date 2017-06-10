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
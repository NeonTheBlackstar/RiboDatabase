def promoters(
	genome_id = sys.argv[1], 					# Genome ID
	genome_fasta = './Genomes/{}.fasta'.format(sys.argv[1]),	# Genome fasta file path
	window = '100', 						# Window size for the upstream region to be compared
	gccontent = 'default'						# GC-content of the whole genome
	):
	
	
	aptamer_list = createAptamersFilter("./Results/{0}.result.csv".format(genome))
	filterWindows(aptamer_list, "aptamer_windows.fasta", "promoter_windows.fasta")

	### PROMPREDICT ###
	gccontent = float(subprocess.check_output("./Programs/gc_calc Genomes/{0}.fasta".format(genome_id), shell=True))

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

			
	### BPROM ###
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

	os.system('rm ./*_PPde.txt')
	os.system('rm ./*_stb.txt')
	os.system('rm ./*_GCstat.txt')
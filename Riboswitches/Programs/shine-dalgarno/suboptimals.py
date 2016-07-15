import sys
import os
import subprocess
import datetime

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def runBarriers(sub_opt_seqs, minimumEnergy): # First argument is rnafold_seq file, second is deltaEnergy parameter
	print('Runs!')
	fasta_seqs = open(sub_opt_seqs,'r') # RNAfold_seqs.fasta file 

	subsequence_fasta = ''
	subopt_input = ''
	gene_id = ''
	directory = ''
	output_file = ''
	fasta_id = ''
	sub_fasta = open('suboptimals.fasta','w')

	flag = False
	for line in fasta_seqs:
		if line[0] == '>':
			### PASS ON GATHERED DATA ###
			if subopt_input != '':
				h_subs = open('subsequence_input.fasta', 'w+')
				h_subs.write(subsequence_fasta)
				h_subs.close()
			
				os.system('mv subsequence_input.fasta ' + '\'Barriers output/' + gene_id + '\'')
				subprocess.getoutput('RNAsubopt -e ' + str(minimumEnergy) + ' -s < \'Barriers output/' + gene_id + '/subsequence_input.fasta\' > \'Barriers output/' + gene_id + '/out.fasta\'')

				# Prepare file for barriers
				handle = open('Barriers output/' + gene_id + '/out.fasta','r')
				h_bar = open('Barriers output/' + gene_id + '/barriers_input.txt','w')
				for _line in handle:
					if(_line[0] != '>'):
						h_bar.write(_line)
				handle.close()
				h_bar.close()
		
				subprocess.getoutput('barriers \'Barriers output/' + gene_id + '/barriers_input.txt\' > barriers_output.txt')
				os.system('mv tree.ps ' + '\'Barriers output/' + gene_id + '\'')
				os.system('mv barriers_output.txt ' + '\'Barriers output/' + gene_id + '\'')
			
				### BARRIERS OUTPUT IS CREATED, SO WE CAN EXTRACT RESULTS AND CHECK WHETEHER SD IS BOUNDED OR NOT ###
				### create fasta with suboptimals
				barr_out = open('Barriers output/' + gene_id + '/barriers_output.txt','r')
			
				count = 0
				current_id = ''
				for _line in barr_out:
					if count == 3:
						break
					temp = ' '.join(_line.split())
					temp = temp.split(' ')
					if is_number(temp[0]) == True:
						if current_id != fasta_id:
							sub_fasta.write(fasta_id)
							current_id = fasta_id
						sub_fasta.write(temp[1]+'\n')
					elif temp[0][0] == '(' or temp[0][0] == ')' or temp[0][0] == '.': # Jesli cala sekwencja zalamalaby sie na kilka linii
						sub_fasta.write(temp[0]+'\n')
					count += 1
				barr_out.close()

				subopt_input = ''
				subsequence_fasta = ''
				os.system('rm -f \'Barriers output/' + gene_id + '/barriers_input.txt\'')
				os.system('rm -f \'Barriers output/' + gene_id + '/out.fasta\'')
				
				### Timestamp ###
				current_time = datetime.datetime.now().time()
				print('Done '+gene_id+', '+str(current_time.isoformat()))
				
			fasta_id = line
			gene_id = line.split('|')[1]
			directory = 'Barriers output/' + gene_id
			output_file = '\'Barriers output/' + gene_id + '/out.fasta' + '\''
		
			if not os.path.exists(directory):
	    			os.makedirs(directory)
		else:
			subopt_input += line.rstrip()
			subsequence_fasta += line.rstrip()
	else:
		h_subs = open('subsequence_input.fasta', 'w+')
		h_subs.write(subsequence_fasta)
		h_subs.close()
			
		os.system('mv subsequence_input.fasta ' + '\'Barriers output/' + gene_id + '\'')
		subprocess.getoutput('RNAsubopt -e ' + str(minimumEnergy) + ' -s < \'Barriers output/' + gene_id + '/subsequence_input.fasta\' > \'Barriers output/' + gene_id + '/out.fasta\'')

		# Prepare file for barriers
		handle = open('Barriers output/' + gene_id + '/out.fasta','r')
		h_bar = open('Barriers output/' + gene_id + '/barriers_input.txt','w')
		for _line in handle:
			if(_line[0] != '>'):
				h_bar.write(_line)
		handle.close()
		h_bar.close()
		#os.system('cd ' + '\'./Barriers output/' + gene_id + '\'')
		
		subprocess.getoutput('barriers \'Barriers output/' + gene_id + '/barriers_input.txt\' > barriers_output.txt')
		os.system('mv tree.ps ' + '\'Barriers output/' + gene_id + '\'')
		os.system('mv barriers_output.txt ' + '\'Barriers output/' + gene_id + '\'')
			
		### BARRIERS OUTPUT IS CREATED, SO WE CAN EXTRACT RESULTS AND CHECK WHETEHER SD IS BOUNDED OR NOT ###
		### create fasta with suboptimals
		barr_out = open('Barriers output/' + gene_id + '/barriers_output.txt','r')
			
		count = 0
		current_id = ''
		for _line in barr_out:
			if count == 3:
				break
			temp = ' '.join(_line.split())
			temp = temp.split(' ')
			if is_number(temp[0]) == True:
				if current_id != fasta_id:
					sub_fasta.write(fasta_id)
					current_id = fasta_id
				sub_fasta.write(temp[1]+'\n')
			elif temp[0][0] == '(' or temp[0][0] == ')' or temp[0][0] == '.': # Jesli cala sekwencja zalamalaby sie na kilka linii
				sub_fasta.write(temp[0]+'\n')
			count += 1
		barr_out.close()

		subopt_input = ''
		subsequence_fasta = ''
		os.system('rm -fr \'./Barriers output\'')
				
		### Timestamp ###
		current_time = datetime.datetime.now().time()
		print('Done '+gene_id+', '+str(current_time.isoformat()))
	sub_fasta.close()
			
#runBarriers('rnafold_seqs.fasta', 3)
import sys
import re

# Gets motives' postions
def getSdFromMeme(*arg):
	f_meme = open(arg[0], 'r') #argv[1]
	f_out = open('meme_output.txt','w')
	initial_window = arg[1]
	counter = -1
	motif = ''
	blocks = True
	motif_pos = ''

	for line in f_meme:
		if re.search('\s+sites sorted by position p-value\s+',line):
			print(line)
			counter = 4 # Need to pass some lines to get to data
		if counter > 0:
			counter -= 1
			continue
		if counter == 0 and line[0] == '-':
			blocks = False
		if counter == 0 and blocks == True:
			formated = re.sub('\s+','\t', line.strip())
			temp = formated.split('\t')
			motif_pos = temp[0]			

			#if re.search('\+',temp[0]) or re.search('-',temp[0]):
			#	_from = initial_window - (int(temp[1]) - 1) # Because in meme position starts from 1, temp[1] is position of SD in window
			#	_to = _from - len(temp[4]) # temp[4] is a length of motif			
			#	motif_pos += '|' + str(_from) + '|' + str(_to) 
				#print(description)
			#elsif re.search('-',temp[0]):
			#	_from = initial_window - (int(temp[1]) - 1) # Because in meme position starts from 1, temp[1] is position of SD in window
			#	_to = _from + len(temp[4]) # temp[4] is a length of motif			
			#	description = temp[0] + '|' + str(_from) + '|' + str(_to) 
			
			_from = initial_window - (int(temp[1]) - 1) # Because in meme position starts from 1, temp[1] is position of SD in window
			_to = _from - len(temp[4]) # temp[4] is a length of motif			
			motif_pos += '|' + str(_from) + '|' + str(_to) 
			
			formated = motif_pos + '\t' + temp[1] + '\t' + temp[2] + '\t' + temp[4] # delete seq that is not motif
			if float(formated.split('\t')[2]) <= 0.05:
				f_out.write(formated+'\n')
	f_meme.close()
	f_out.close()

# _from and _to are offset positions of SD motif due to position of codon start


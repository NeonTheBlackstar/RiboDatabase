import os
import sys

xD = open('output_7.txt','r')
print('sss')

for file in os.listdir('./bprom'):
	if file.startswith('output'):
		with open(file) as file_h:
			gene_name = ''
			promoterExists = False

			for line in file_h:
				if line.strip().startswith('>'):
					gene_name = line.strip().split('|')[3]
					continue
				if int( line.strip().split('-')[1].strip() ) > 0:
					print(gene_name)
					break
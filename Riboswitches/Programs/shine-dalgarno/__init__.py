import sys
import os
import subprocess
import sd2
import get_sd2
import suboptimals
import find_switch
import filter

### EXAMPLE OF USING
# python3 __init__.py '../../Genomes/bacillus.gff' '../../Genomes/NC_000964.3.fasta' nomeme

# Set isMeme to false only if meme_output.txt is already generated and you don't want to overwrite motif data!
def runShineDalAnalysis(genome_id, isMeme):
	file_gff = './Genomes/' + genome_id + '.gff'	# String path for gff genome annotation file
	gff_handle = open(file_gff, 'r')
	file_fasta = './Genomes/' + genome_id + '.fasta' 	# String path for fasta genome sequence file
	file_ptt = './Results/' + genome_id + '.ptt'
	file_bed = './Results/' + genome_id + '.terminators.bed'
	
	filter_dictionary = filter.createGffFilter(file_ptt, file_bed)

	if(bool(filter_dictionary) != False):	
		if isMeme == True:									### Skip meme step with 'nomeme' switch if 'meme_output.txt' file is generated!
			print(filter_dictionary)
			input()
			filter_dictionary = filter.prepareSample(filter_dictionary, file_gff)		# Create sample filter for meme
			print(filter_dictionary)
			print(len(filter_dictionary))

			sd2.getFasta(file_gff, file_fasta, 25, filter_dictionary)			# Prepare data for meme
			os.system('meme shi-dal_output.fasta -w 8 -mod oops -dna -maxsize 200000') 	# Run meme
			get_sd2.getSdFromMeme('./meme_out/meme.txt', 25)				# Extract motifs data from meme
			os.system('mv meme_output.txt ./Programs/shine-dalgarno/meme_output.txt')
			#os.system('rm -fr meme_out')
			input()
			filter_dictionary = filter.createGffFilter(file_ptt, file_bed)			# Overwrite filter for structures

		sd2.getFasta(file_gff, file_fasta, 100, 50, './Programs/shine-dalgarno/meme_output.txt', filter_dictionary)	# Prepare data for RNA-fold/Barriers
		suboptimals.runBarriers('rnafold_seqs.fasta', 3)					# Run Barriers and produce fasta output of secondary RNA structure
		find_switch.findSwitch(0.6, file_gff, genome_id)					# Check whether genes' suboptimal structures have a form of ryboswitch, if they do - print adnotations to related genes to .bed file
	
		os.system('rm -f rnafold_seqs.fasta')
		os.system('rm -f suboptimals.fasta')
	else:
		print('Brak terminacji translacyjnej, gdyz znaleziono terminatory dla wszystkich aptamerow.')

import csv

'''
This script reads csv file and divides it to lists. Every row in csv file is a single list. 
Script uses lists in list construction.
First list contains names of columns in csv file. Proper data starts from the secon list (first index).

Lack of the values in csv file is displayed as a empty quotes.

Column names: ligand [0], class [1], name [2], organism [3], gene [4], operon [5], mechanism [6], effect [7], confirmation of mechanism [8],
position in genome [9], sequence [10], secondary structure [11], 3D structure [12], other references [13] (indexed from one :, so e.g. l[1][5], l[2][0] etc.).

Examples:
l[2][1] is a class name of second switch in csv file
l[4][7] is an effect which has eight switch in csv file
'''
def csvParser(fileName):
	spamReader = csv.reader(open(fileName, newline = ''), delimiter = '\t') #construction for Python3
	return [list(row) for row in spamReader]
	#l = l[1:] - if you want to delete first list which contains names of the colums
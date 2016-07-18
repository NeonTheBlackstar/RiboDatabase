import csv

'''
This script reads csv file and divides it to lists. Every row in csv file is a single list. 
Script uses lists in list construction.
First list contains names of columns in csv file. Proper data starts from the secon list (first index).

Lack of the values in csv file is displayed as a empty quotes.

Column names: ligand, class, name, organism, gene, operon, mechanism, effect, confirmation of mechanism,
position in genome, sequence, secondary structure, 3D structure, other references (indexed from one :).

Examples:
l[2][1] is a class name of second switch in csv file
l[4][7] is an effect which has eight switch in csv file
'''

l = []
spamReader = csv.reader(open('switche2.csv', newline = ''), delimiter = '\t') #construction for Python3
temp_l = []
for row in spamReader: #we read ech row in csv file
	temp_l.append(row)
	temp_l = list(temp_l[0]) #single index list division
	l.append(temp_l)
	temp_l = []
	#l = l[1:] - if you want to delete first list which contains names of the colums

print(l[0])
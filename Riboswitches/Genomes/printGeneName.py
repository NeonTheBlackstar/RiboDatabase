# BSU30550
# protein_coding

from BCBio import GFF
import sys
import os

locuses = sys.argv[1:]
handle = open('NC_000964.3.gff')

for l in locuses:
	for record in GFF.parse(handle):
		for feature in record.features:
			if 'locus_tag' in feature.qualifiers and feature.qualifiers['locus_tag'][0] == l: 
				#and feature.qualifiers['locus_tag'] == l:
				print(feature.qualifiers['gene'])

import os
import sys


def isParameter(param, param_list):
	for i in range(0,len(param_list)):
		if param_list[i] == param:
			return True
	return False


gramNeg = isParameter('neg',sys.argv)						# ValueType: Boolean
gramPos = isParameter('pos',sys.argv)						# ValueType: Boolean
sumUp = isParameter('sum',sys.argv)							# ValueType: Boolean

classes_dic = {}
lista = os.listdir('Alignments')

for i in range(0, len(lista)):
	class_name = ""
	with open("./Alignments/{0}".format(lista[i])) as class_handle:
		for line in class_handle:
			line = line.strip()
			if line.startswith("NAME"):
				class_name = line.split()[1]
				classes_dic[class_name] = 0 # So you can increment
				break

genomes_list = []
with open("logs.csv") as logs_handle:
	for line in logs_handle:
		line = line.strip()
		row_list = line.split('\t')

		genome_id = row_list[0]
		org_name = row_list[1]
		genome_dic = {
			'name': org_name,
			'gram': row_list[6],
			'riboswitches': classes_dic.copy()
		}
		with open("./Results/{0}.result.csv".format(genome_id)) as results_handle:
			lines_r = results_handle.readlines()[1:]
			new_lines_r = []
			# Remove duplicated results
			row_dic = {}

			for line_r in lines_r:
				line_r = line_r.strip()
				row_list_r = line_r.split('\t')
				gene_name = row_list_r[3]

				if gene_name not in row_dic:
					row_dic[gene_name] = {
						'score': float(row_list_r[14]),
						'line': line_r
					}
				else:
					score = float(row_list_r[14])
					if row_dic[gene_name]['score'] > score:
						row_dic[gene_name] = {
							'score': float(row_list_r[14]),
							'line': line_r
						}

			new_lines_r = [row_dic[key]['line'] for key in row_dic]
			
			'''with open("test.csv", 'w') as test:
				for line in new_lines_r:
					test.write(line+"\n")
			print(new_lines_r)
			break'''
			###
			for line_r in new_lines_r:

				line_r = line_r.strip()
				row_list_r = line_r.split('\t')
				class_name_r = row_list_r[9]
				#print(class_name_r)

				genome_dic['riboswitches'][class_name_r] += 1

		genomes_list.append(genome_dic)

sum_classes = {}
prefix = ""
if gramPos and not gramNeg:
	prefix = "pos_"
elif not gramPos and gramNeg:
	prefix = "neg_"
elif gramPos and gramNeg:
	prefix = "all_"
sufix = ""
if sumUp:
	sufix = "sum_"

with open("{}{}piechart_output.csv".format(prefix, sufix), "w") as charts_handle:
	classes_list = sorted(classes_dic.keys())
	if sumUp == True:
		charts_handle.write("\t".join(classes_list) + "\n" )
	else:
		charts_handle.write("Organism\t" + "\t".join(classes_list) + "\n" )
	for org in genomes_list:
		if (gramPos == True and org['gram'] == "pos") or (gramNeg == True and org['gram'] == "neg"):
			if not sumUp:
				charts_handle.write(org['name']) # org['gram']
				for class_ in classes_list:
					charts_handle.write('\t'+str(org['riboswitches'][class_]))
				charts_handle.write('\n')
			else:
				for class_ in classes_list:
					if class_ not in sum_classes:
						sum_classes[class_] = org['riboswitches'][class_]
					else:
						sum_classes[class_] += org['riboswitches'][class_]
	
	if sumUp == True:
		for class_ in classes_list:
			charts_handle.write(str(sum_classes[class_])+'\t')
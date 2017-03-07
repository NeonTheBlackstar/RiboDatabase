f = open("ribsw_pos_window.fasta")
out = open("out.fasta", "w+")

for line in f:
	for i in range(0,10):
		#print(i)
		line = line.replace(str(i), "")
	out.write(line)

f.close()
out.close()
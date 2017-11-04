import sys

with open(sys.argv[1]) as handle, open(sys.argv[1].split('.')[0]+"_converted.txt", 'w') as out:
	next(handle)
	for line in handle:
		_list = line.strip().split('\t')
		if len(_list) != 2 and _list[1] != "\"\"":
			out.write("{}\t{}\n".format(_list[-1][1:-1], _list[1]))
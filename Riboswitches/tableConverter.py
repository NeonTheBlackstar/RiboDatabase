import sys

with open(sys.argv[1]) as handle, open(sys.argv[1].split('.')[0]+"_converted.txt", 'w') as out:
	next(handle)
	
	for line in handle:
		_list = line.split('\t')

		if sys.argv[2] == "bsub":
			if not (_list[1] != "\"\"" and ":EV-EXP" not in _list[2]):
				out.write("{}\t{}\n".format(_list[0], _list[1]))
		elif sys.argv[2] == "ecoli":
			if _list[0] != "" and not (_list[1] != "\"\"" and ":EV-EXP" not in _list[2]):
				out.write("{}\t{}\n".format(_list[0][1:-1], _list[1]))
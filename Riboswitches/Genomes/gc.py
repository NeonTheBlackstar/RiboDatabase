import sys

f = open(sys.argv[1])
count = 0
gc = 0
for line in f:
	line = line.strip()
	if not line.startswith('>'):
		for nuc in line:
			if nuc == "G" or nuc == "C":
				gc += 1
			count += 1

result = 100 * gc / count
print("{}%".format(result))
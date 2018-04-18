import sys
import os
# Programs/rnamotif-3.1.1/src/rnamotif -descr sd3p.descr AU_THIC.fasta > sd3p.output
# python3 descriptorTest.py sequences_THI_ribswitch.fasta sd3p.descr sd5p.descr

descriptorsList = sys.argv[2:]
seqsFile = sys.argv[1]

seq = ""
total = 0
found = 0
with open(seqsFile) as s:
	for l in s:
		l = l.strip()
		if l.startswith(">"):
			if seq != "":
				total += 1
				motif = seq[mStart:mEnd]

				isHarpin = False
				diry = "RNAmotif/{}".format(mName)
				os.system("mkdir " + diry + " > /dev/null 2>&1")
				for f in descriptorsList:
					newDesc = "{}_m.descr".format(f.split(".")[0])
					with open(f) as h, open(newDesc,'w') as o:
						for line in h:
							if "seq=" in line:
								sp = line.split("seq=\"\"")
								line = "{} seq=\"{}\"{}".format(sp[0], motif, sp[1])
							o.write(line)
					os.system("rm desc.out")					
					os.system("Programs/rnamotif-3.1.1/src/rnamotif -descr {} {} > desc.out".format(newDesc, seqsFile))					
					
					### Save found structures ###
					os.system("rm {}/{}".format(diry, "{}.out".format(f.split(".")[0])))
					os.system("cp {} {}/{}".format("desc.out", diry, "{}.out".format(f.split(".")[0])))
					
					with open("desc.out") as descOut:
						for ln in descOut:
							if ln.startswith("#"):
								isHarpin = True
				if isHarpin == True:
					print(mName, motif, mStart, mEnd)
					found += 1
				else:
					print("########", mName, motif, mStart, mEnd)
					
			temp = l.split(":")
			mName = temp[0][1:]
			mStart = int(temp[1]) - 1
			mEnd = int(temp[2]) - 1
		elif not l.startswith(">"):
			seq = l

print("Total:", total, "Found:", found, "Percent:", found * 100 / total, "%")
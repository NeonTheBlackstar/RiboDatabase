from BCBio import GFF
from glob import glob
import os
import re
import sys
import linecache
import subprocess
sys.path.insert(0, './Programs/shine-dalgarno')
import __init__
import sd2
import new_sd2
import get_sd2
from datetime import datetime, timedelta
from time import sleep, localtime, strftime
### HOW TO USE ###
# python3 mainscript.py NC_000964.3
# Programs/meme_4.12.0/src/meme
# awk 'BEGIN {OFS = ""} {if($1 ~ /^>/) { print $1,"|"; } else {print;}}' sequences_THI_ribswitch.fasta

inputFasta = sys.argv[1]

# Extract 25-nucleotide window, which ends in TSS position
os.system("""awk 'BEGIN {OFS = ""; FS = ":|\|"} { if($1 ~ /^>/) { tss = $4; print; } else { print substr($0, tss - 25, 25); }}' """+ inputFasta +""" > inputSeqsMEME.fasta""")
# Run MEME on sequences of given window
os.system('sudo {} {} -w 6 -mod oops -dna -maxsize 200000'.format("Programs/meme/src/meme", "inputSeqsMEME.fasta"))
# Extract motif data from MEME output
get_sd2.getSdFromMeme('./meme_out/meme.txt', 25) 



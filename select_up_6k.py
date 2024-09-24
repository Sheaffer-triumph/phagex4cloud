#!/usr/bin/env python3
import sys,re
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--fasta", dest="filename",help="Assembly fasta")
parser.add_option("-c", "--cutoff", dest="cutoff", help="select >cutoff length scaffolds")

(options, args) = parser.parse_args()
#print(options.filename)
dict1={}
with open(options.filename,'r') as f1:
    for line in f1.readlines():
        line=line.strip()
        if re.search('>',line) :
            ID=line
            dict1[ID]=[]
        else:
            dict1[ID].append(line)

for key in sorted(dict1.keys()):
    seq="".join(dict1[key])
    if len(seq) >= int(options.cutoff):
        print(key,seq,sep='\n',end='\n')   
        

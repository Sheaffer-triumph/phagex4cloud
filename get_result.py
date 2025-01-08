#!/bin/env python3
import os
import sys

blast_result = sys.argv[1]
hmm_result = sys.argv[2]
out_path = sys.argv[3]

to_write_dict = {}
with open(blast_result) as f:
	for line in f.readlines():
		text_splits = line.split('\t')
		seq_name = text_splits[0]
		protein_id = text_splits[1]
		product = text_splits[2]
		identity = text_splits[3]
		evalue = text_splits[-2]
		method = 'blast'
		line = '\t'.join([seq_name,protein_id,product,identity,evalue,method])+'\n'
		#print(line)
		to_write_dict[seq_name]=line

with open(hmm_result) as f:
	for line in f.readlines():
		text_splits = line.split(None,18)
		seq_name = text_splits[2]
		protein_id = text_splits[0]
		product = text_splits[-1].strip()
		identity = 'Na'
		evalue = text_splits[7]
		method = 'hmmer'
		line = '\t'.join([seq_name,protein_id,product,identity,evalue,method])+'\n'
		if seq_name not in to_write_dict.keys():
			to_write_dict[seq_name]=line
with open(out_path,'w') as f_w:
	for value in to_write_dict.values():
		f_w.write(value)

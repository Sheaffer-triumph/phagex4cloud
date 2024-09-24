#!/bin/env python3
import os
import sys

source_path = sys.argv[1]
target_path = sys.argv[2]

evalue_dict = {}
to_write_dict = {}
with open(source_path) as f:
	for line in f.readlines():
		text_splits = line.split(None,18)
		protein_name = text_splits[2]
		evalue = text_splits[4]
		if protein_name not in evalue_dict.keys():
			evalue_dict[protein_name] = evalue
			to_write_dict[protein_name] = line
		elif evalue < evalue_dict[protein_name]:
			evalue_dict[protein_name] = evalue
			to_write_dict[protein_name] = line

with open(target_path,'w') as f_w:
	for value in sorted(to_write_dict):
		f_w.write(to_write_dict[value])

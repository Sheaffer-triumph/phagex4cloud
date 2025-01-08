#!/bin/env python3
import sys

result_txt_path = sys.argv[1]
gff_path = sys.argv[2]
out_path = sys.argv[3]

info_dict = {}
with open(result_txt_path) as f:
	for line in f.readlines():
		line_splits = line.split('\t')
		####NODE_1_length_30728_cov_33.714691####
		#ID = '_'.join([line_splits[0].split('_')[1],line_splits[0].split('_')[-1]])
		####id中只有一个下划线####
		ID = '_'.join(["1",line_splits[0].split('_')[-1]])
		protein_id = line_splits[1]
		product = line_splits[2].replace('=',':')
		insert = "protein_id={0};product={1};".format(protein_id,product)
		#print("^^^",ID)
		info_dict[ID] = insert

to_write_dict = {}
with open(gff_path) as f:
	for line in f.readlines():
		if not line.startswith('#'):
			ID = line.split('\t')[-1].split(';')[0].split('=')[1]
			#print("@@@@",ID)
			if ID in info_dict.keys():
				line = '\t'.join(line.split('\t')[:-1])+'\t'+info_dict[ID]+'\n'
				to_write_dict[ID] = line
			else:
				print("No hit found:{}".format(ID))
				#old verison
				#line = '\t'.join(line.split('\t')[:-1])+'\t'+'\n'
				#add UNA 
				line = '\t'.join(line.split('\t')[:-1])+'\tprotein_id=UNA;product=Unaligned protein '+ID+';\n'
				to_write_dict[ID] = line

with open(out_path,'w') as f_w:
	for value in to_write_dict.values():
		f_w.write(value)


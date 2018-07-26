import sys
import os
uni_shr = sys.argv[1]

pro_dic = dict()
f1 = open('DTBP-_first_category.txt_hs_'+uni_shr,'r')
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f1.close()
pro_list = list()
f2 = open('DTBP-_second_category.txt_hs_'+uni_shr,'r')
for line in f2:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f2.close()
pro_list = list()
f3 = open('DTBP+_first_category.txt_hs_'+uni_shr,'r')
for line in f3:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f3.close()
pro_list = list()
f4 = open('DTBP+_second_category.txt_hs_'+uni_shr,'r')
for line in f4:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f4.close()
pro_list = list()
f6 = open('MUCUS_first_category.txt_hs_'+uni_shr,'r')
for line in f6:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f6.close()
pro_list = list()
f5 = open('MUCUS_second_category.txt_hs_'+uni_shr,'r')
for line in f5:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pro_token = token[1].split('; ')
		if token[0] in pro_dic:
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
		else:
			pro_dic[token[0]] = list()
			for i in range(0,len(pro_token)):
				pro_dic[token[0]].append(pro_token[i])
			pro_dic[token[0]] = list(set(pro_dic[token[0]]))
f5.close()

fo2 = open('name_sort_hs_'+uni_shr,'w')
fo2.write('#pep_ID\tXL_ID\n')
for k,v in pro_dic.items():
	fo2.write(k+'\t'+'; '.join(pro_dic[k][0:len(pro_dic[k])])+'\n')
fo2.close()

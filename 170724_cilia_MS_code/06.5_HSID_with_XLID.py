import sys
uni_shr = sys.argv[1]

pro_pep_dic = dict()
f1 = open('DTBP-_first_category.txt','r')
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f1.close()
pro_list = list()
f2 = open('DTBP-_second_category.txt','r')
for line in f2:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f2.close()
pro_list = list()
f3 = open('DTBP+_first_category.txt','r')
for line in f3:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f3.close()
pro_list = list()
f4 = open('DTBP+_second_category.txt','r')
for line in f4:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f4.close()
pro_list = list()
f6 = open('MUCUS_first_category.txt','r')
for line in f6:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f6.close()
pro_list = list()
f5 = open('MUCUS_second_category.txt','r')
for line in f5:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[1] == '-':
			pro_token = token[1].split('; ')[1]
		elif not token[2] == '-':
			pro_token = token[2]
		if pro_token in pro_pep_dic:
			pro_pep_dic[pro_token].append(token[0])
		else:
			pro_pep_dic[pro_token] = list()
			pro_pep_dic[pro_token].append(token[0])
f5.close()

for k,v in pro_pep_dic.items():
	n_v = list(set(v))
	pro_pep_dic[k] = n_v

pep_id_dic = dict()
f7 = open('name_sort_hs_'+uni_shr,'r')
for line in f7:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		pep_id_dic[token[0]] = token[1].split('; ')
f7.close()

n_dic = dict()
for k,v in pro_pep_dic.items():
	n_dic[k] = list()
	for i in range(0,len(v)):	
		if v[i] in pep_id_dic:
			n_dic[k] += n_dic[k] + pep_id_dic[v[i]]
			n_dic[k] = list(set(n_dic[k]))

fo2 = open('HSID_with_XLID_hs_'+uni_shr,'w')
fo2.write('#HS_ID\tXL_ID\n')
for k,v in n_dic.items():
	fo2.write(k+'\t'+'; '.join(n_dic[k][0:len(n_dic[k])])+'\n')
fo2.close()

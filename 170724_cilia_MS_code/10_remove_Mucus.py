f1 = open('Xenopus laevis cilia isolation protein count_HS','r')
f2 = open('Mucus_except_list','r')
f1.readline()
f1_dic = dict()
f2_list = list()

for line in f1:
	token = line.strip().split('\t')
	f1_dic[token[0]] = '\t'.join(token[1:7])
f1.close()
for line in f2:
	token = line.strip()
	f2_list.append(token)
f2.close()

for k,v in f1_dic.items():
	if not k in f2_list:
		token = v.split('\t')
		if not token[0] == '0':
			del f1_dic[k]

f_o = open('HS_XL_Mucus_filtered','w')
f_o.write('#Xenopus laevis protein ID\tMucos_1\tMucos_2\tDTBP-_1\tDTBP-_2\tDTBP+_1\tDTBP+_2\n')
for k,v in f1_dic.items():
	f_o.write(k+'\t'+v+'\n')
f_o.close()

f1 = open('DTBP_p','r')
f2 = open('DTBP_m','r')
f3 = open('MUCUS','r')
f1_dic = dict()
f2_dic = dict()
f3_dic = dict()
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		f1_dic[token[0]] = token[1]+'\t'+token[2]
for line in f2:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		f2_dic[token[0]] = token[1]+'\t'+token[2]
for line in f3:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		f3_dic[token[0]] = token[1]+'\t'+token[2]
f1.close()
f2.close()
f3.close()

n_dic = dict()

for k,v in f1_dic.items():
	if not k in f2_dic and not k in f3_dic:
		n_dic[k] = '0'+'\t'+'0'+'\t'+'0'+'\t'+'0'+'\t'+v
	elif k in f2_dic and not k in f3_dic:
		n_dic[k] = '0'+'\t'+'0'+'\t'+f2_dic[k]+'\t'+v
	elif not k in f2_dic and k in f3_dic:
		n_dic[k] = f3_dic[k]+'\t'+'0'+'\t'+'0'+'\t'+v
	elif k in f2_dic and k in f3_dic:
		n_dic[k] = f3_dic[k]+'\t'+f2_dic[k]+'\t'+v
for k,v in f2_dic.items():
	if not k in f1_dic and not k in f3_dic:
		n_dic[k] = '0'+'\t'+'0'+'\t'+v+'\t'+'0'+'\t'+'0'
	elif not k in f1_dic and k in f3_dic:
		n_dic[k] = f3_dic[k]+'\t'+v+'\t'+'0'+'\t'+'0'
for k,v in f3_dic.items():
	if not k in f1_dic and not k in f2_dic:
		n_dic[k] = v+'\t'+'0'+'\t'+'0'+'\t'+'0'+'\t'+'0'
		
f_o = open('Xenopus laevis cilia isolation protein count_HS','w')
f_o.write('Xenopus laevis protein ID\tMucos_1\tMucos_2\tDTBP-_1\tDTBP-_2\tDTBP+_1\tDTBP+_2\n')
for k,v in n_dic.items():
	f_o.write(k+'\t'+v+'\n')
f_o.close
print 'done'

f1 = open('TMHMM_result','r')
f2 = open('HS_XL_Mucus_filtered_log10','r')
f2.readline()
f1_dic = list()
for line in f1:
	token = line.strip().split('\t')
	if not token[5] == 'Topology=o' and not token[5] == 'Topology=i':
		f1_dic.append(token[0])

f_o = open('TMHMM_HS_XL_Mucus_filtered_log10','w')
f_o.write('#name\tMucos_1\tMucos_2\tDTBP-_1\tDTBP-_2\tDTBP+_1\tDTBP+_2\n')
for line in f2:
	token = line.strip().split('\t')
	if token[0] in f1_dic:
		f_o.write('O'+'\t'+line)
	else:
		f_o.write('X'+'\t'+line)

f_o.close()


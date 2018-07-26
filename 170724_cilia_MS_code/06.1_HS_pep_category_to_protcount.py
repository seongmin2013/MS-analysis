import sys
import re
filename_txt = sys.argv[1]
f1 = open(filename_txt,'r')

pro_dic = dict()
sh_pro_dic = dict()
pro_list = list()
pep_dic = dict()
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		count = int(token[4])
		pep = token[0]
		if not token[1] == '-':
			hs_id = token[1].split('; ')[1]
			if hs_id in pep_dic:
				pep_dic[hs_id].append(pep)
			else:
				pep_dic[hs_id] = list()
				pep_dic[hs_id].append(pep)
			if hs_id in pro_dic:
				pro_dic[hs_id] += count
			else:
				pro_dic[hs_id] = count
				pro_list.append(hs_id)
		elif not token[2] == '-':
			hs_id = token[2]
			if hs_id in pep_dic:
				pep_dic[hs_id].append(pep)
			else:
				pep_dic[hs_id] = list()
				pep_dic[hs_id].append(pep)
			if hs_id in pro_dic:
				pro_dic[hs_id] += count
			else:
				pro_dic[hs_id] = count
				pro_list.append(hs_id)
		else:
			pro_token = token[3].split('; ')
			for i in range(0,len(pro_token)):
				hs_id = pro_token[i]
				if hs_id in pep_dic:
					pep_dic[hs_id].append(pep)
				else:
					pep_dic[hs_id] = list()
					pep_dic[hs_id].append(pep)
				if pro_token[i] in sh_pro_dic:
					sh_pro_dic[hs_id] += count
				else:
					sh_pro_dic[hs_id] = count
					pro_list.append(hs_id)
f1.close()

pro_list = list(set(pro_list))

fo = open(filename_txt+'_count','w')
fo.write('#protID\tHSunique\tHSshared\tpeptide\n')
for k in pro_list:
	if k in pro_dic and k in sh_pro_dic:
		fo.write(k+'\t'+str(pro_dic[k])+'\t'+str(sh_pro_dic[k])+'\t'+'; '.join(pep_dic[k][0:len(pep_dic[k])])+'\n')
	elif k in pro_dic and not k in sh_pro_dic:
		fo.write(k+'\t'+str(pro_dic[k])+'\t'+'0'+'\t'+'; '.join(pep_dic[k][0:len(pep_dic[k])])+'\n')
	elif not k in pro_dic and k in sh_pro_dic:
		fo.write(k+'\t'+'0'+'\t'+str(sh_pro_dic[k])+'\t'+'; '.join(pep_dic[k][0:len(pep_dic[k])])+'\n')
fo.close()

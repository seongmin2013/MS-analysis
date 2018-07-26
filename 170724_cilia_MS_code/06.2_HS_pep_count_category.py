import sys
import re
filename_txt = sys.argv[1]
f1 = open(filename_txt,'r')

pep_dic = dict()
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')		
		pep_dic[token[0]] = int(token[1])
f1.close()

hs_dic = dict()
f2 = open('/home/seongmin/Desktop/computational/proteomics/data/Xenopus/XENLA_JGIv18pV2_prot_finalHS.fasta','r')
for line in f2:
    if line.startswith('>'):
        tmp = line.strip().lstrip('>')
	head = tmp.split('|')[1].split('=')[1]
	if head == 'NA':
		continue
        hs_dic[tmp] = ''
    else:
	if head == 'NA':
		continue
        hs_dic[tmp] += line.strip()
f2.close()

tmp_count = 1
hs_pep_name = dict()
xl_pep_name = dict()
for hs,hs_seq in hs_dic.items():
	for pep in pep_dic.keys():
		if pep in hs_seq:
			if not pep in hs_pep_name:
				hs_pep_name[pep] = list()
				hs_pep_name[pep].append(hs.split('HS=')[1].split('|')[0])
			else:
				hs_pep_name[pep].append(hs.split('HS=')[1].split('|')[0])
			if not pep in xl_pep_name:
				xl_pep_name[pep] = list()
				xl_pep_name[pep].append(hs.split('|')[0]+'|'+hs.split('|')[-1]+'; '+hs.split('HS=')[1].split('|')[0])
			else:
				xl_pep_name[pep].append(hs.split('|')[0]+'|'+hs.split('|')[-1]+'; '+hs.split('HS=')[1].split('|')[0])
	if( tmp_count % 1000 == 0 ):
        	sys.stderr.write('Read %d seq: %s\n'%(tmp_count,hs))
   	tmp_count += 1

uu_xl_name = dict()
xl_share_name = list()
u_hs_name = dict()
s_hs_name = dict()
for k,v in xl_pep_name.items():
	if len(set(v)) == 1:
		if k in uu_xl_name:
			uu_xl_name[k] = uu_xl_name[k] + xl_pep_name[k]
			uu_xl_name[k] = list(set(uu_xl_name[k]))
		else:
			uu_xl_name[k] = list()
			uu_xl_name[k] = uu_xl_name[k] + xl_pep_name[k]
			uu_xl_name[k] = list(set(uu_xl_name[k]))
	else:
		xl_share_name.append(k)

for k,v in hs_pep_name.items():
	if not k in xl_share_name:
		continue
	if len(set(v)) == 1:
		if k in u_hs_name:
			u_hs_name[k] = u_hs_name[k] + hs_pep_name[k]
			u_hs_name[k] = list(set(u_hs_name[k]))
		else:
			u_hs_name[k] = list()
			u_hs_name[k] = u_hs_name[k] + hs_pep_name[k]
			u_hs_name[k] = list(set(u_hs_name[k]))	
	elif len(set(v)) == 0:
		print k
	elif len(set(v)) > 1:
		if k in s_hs_name:
			s_hs_name[k] = s_hs_name[k] + hs_pep_name[k]
			s_hs_name[k] = list(set(s_hs_name[k]))
		else:
			s_hs_name[k] = list()
			s_hs_name[k] = s_hs_name[k] + hs_pep_name[k]
			s_hs_name[k] = list(set(s_hs_name[k]))	
			
fo2 = open(filename_txt.replace('#pepSpectrum.txt','HS_pep_category'),'w')
fo2.write('#pepID\tXLuniqueID\tHSuniqueID\tHSsharedID\tpep_count\n')
for k,v in pep_dic.items():
	if k in uu_xl_name:
		fo2.write(k+'\t'+'; '.join(uu_xl_name[k][0:len(uu_xl_name[k])])+'\t'+'-'+'\t'+'-'+'\t'+str(v)+'\n')
	else:
		if k in u_hs_name:
			fo2.write(k+'\t'+'-'+'\t'+'; '.join(u_hs_name[k][0:len(u_hs_name[k])])+'\t'+'-'+'\t'+str(v)+'\n')
		elif k in s_hs_name:
			fo2.write(k+'\t'+'-'+'\t'+'-'+'\t'+'; '.join(s_hs_name[k][0:len(s_hs_name[k])])+'\t'+str(v)+'\n')
fo2.close()

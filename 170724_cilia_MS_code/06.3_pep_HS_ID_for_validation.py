import sys
import re
filename_txt = sys.argv[1]
uni_shr = sys.argv[2]
f1 = open(filename_txt,'r')

pep_dic = dict()
for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		if not token[3] == '-':		
			pep_dic[token[0]] = token[0]
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
hs_xl_name = dict()
for hs,hs_seq in hs_dic.items():
	for pep in pep_dic.keys():
		if pep in hs_seq:
			if not pep in hs_pep_name:
				hs_pep_name[pep] = list()
				hs_pep_name[pep].append(hs)
			else:
				hs_pep_name[pep].append(hs)
	if( tmp_count % 1000 == 0 ):
        	sys.stderr.write('Read %d seq: %s\n'%(tmp_count,hs))
   	tmp_count += 1
			
fo2 = open('./id_sort/'+filename_txt+'_hs_'+uni_shr,'w')
fo2.write('#pepID\tXLuniqueID\n')
for k,v in hs_pep_name.items():
	fo2.write(k+'\t'+'; '.join(v[0:len(v)])+'\n')
fo2.close()

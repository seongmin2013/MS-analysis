import numpy
import sys
filename_txt = sys.argv[1]
f1 = open(filename_txt,'r')
f2 = open('/home/seongmin/Desktop/computational/proteomics/data/Xenopus/XENLA_JGIv18pV2_prot_finalHS.fasta','r')
fname = f1.name.replace('_#pepSpectrum.txt','')
fname = fname.replace('_#prot','').replace('_pep_category_count','')

s_count = dict()
u_count = dict()
pro_len = dict()
pro_list = dict()
for line in f1:
	if not line.startswith('#'):
		tokens = line.strip().split("\t")
		prot_id = tokens[0]
		s_count[prot_id] = float(tokens[2])
		u_count[prot_id] = float(tokens[1])

for line in f2:
	if(line.startswith('>')):
		pro_h = line.strip().split('|')[1].split('=')[1]
		if not pro_h in pro_list:
			pro_list[pro_h] = list()
	else:
		pro_list[pro_h].append(line.strip())
f1.close()
f2.close()

for k,v in pro_list.items():
	tmp = 0
	for i in range(0,len(v)):
		tmp += len(v[i])
	pro_len[k] = tmp*1.0/len(v)

for k in pro_len.keys():
	if (not k in u_count):
		del pro_len[k]
        
s_list = sorted(s_count.items())
u_list = sorted(u_count.items())
p_list = sorted(pro_len.items())

s_v = []
u_v = []
p_v = []

for k, v in s_list:
    s_v.append(float(v))
for k, v in u_list:
    u_v.append(float(v))
for k, v in p_list:
    p_v.append(float(v))
    
saf = dict()
sum_saf = 0
sum_uspc = 0
nsaf = dict()
for k,v in pro_len.items():
	sum_uspc += 1.0*u_count[k]/pro_len[k]
for k,v in pro_len.items():
	saf[k] = (u_count[k]+(((u_count[k]/pro_len[k])/sum_uspc)*s_count[k]))/pro_len[k]
	sum_saf += saf[k]
for k,v in pro_len.items():
	if not saf[k] == 0:
		nsaf[k] = saf[k]/sum_saf

f1_out = open('%s_protcount_normalization.txt'%fname,'w')
f1_out.write("#name\toutput\tNSAF\n")
for k,v in nsaf.items():
	f1_out.write(k+'\t'+str(u_count[k])+'\t'+str(v)+'\n')
f1_out.close()
print 'Done'

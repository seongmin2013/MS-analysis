f1 = open('HS_XL_Mucus_filtered_log10_5.1','r')
f2 = open('/home/seongmin/Desktop/computational/proteomics/data/human/human_protein.fasta','r')
f1.readline()

seq_h = ''
seq_data = dict()

for line in f2:
	if(line.startswith('>')):
		seq_h = line.strip().split('=')[-3].split(' ')[0]
		seq_data[seq_h] = ''
	else:
		seq_data[seq_h] += line.strip()

data_t1 =dict()

for line in f1:
	if (line.startswith('#')):
		continue
	if(line.strip() in seq_data):
		data_t1[line.strip()] = seq_data[line.strip()]

f_out1 = open(f1.name.split('_')[0]+ "_sequence",'w')
for k,v in data_t1.items():
	f_out1.write('>' + k + '\n' + v.replace('*','') + '\n')
f_out1.close()


print 'done'

f1.close()
f2.close()

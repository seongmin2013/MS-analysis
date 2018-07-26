import sys
filename_txt = sys.argv[1]
filename_txt2 = sys.argv[2]
filename_txt2_head = filename_txt2.readline()

f1 = open(filename_txt,'r')
f2 = open(filename_txt2,'r')
f1_dict = dict()
f2_dict = dict()


for line in f1:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		f1_dict[token[0].upper()] = token[0]

for line in f2:
	if not line.startswith('#'):
		token = line.strip().split('\t')
		f2_dict[token[0].upper()] = '\t'.join(token[1:len(token)])

f1o = open(filename_txt2+'_'+filename_txt+'_filter','w')
f1o.write(filename_txt2_head)
for k,v in f2_dict.items():
	if k in f1_dict:
		f1o.write(k+'\t'+v+'\n')

f1.close()
f2.close()
f1o.close()

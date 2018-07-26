import sys
filename_txt = sys.argv[1]
filename_txt2 = sys.argv[2]
f1 = open(filename_txt,'r')
f2 = open(filename_txt2,'r')
f1.readline()
f2.readline()

f1_list = dict()
f2_list = dict()

for line in f1:
        tokens = line.strip().split("\t")
        f1_list[tokens[0]] = tokens[1]
for line in f2:
        tokens = line.strip().split("\t")
        f2_list[tokens[0]] = tokens[1]
f1.close()
f2.close()

n_dic = dict()
for k,v in f1_list_log.items():
	if k in f2_list_log:
		n_dic[k] = v+'\t'+f2_list[k]
	if not k in f2_list:
		n_dic[k] = v+'\t'+'0'
for k,v in f2_list.items():
	if not k in f1_list:
		n_dic[k] = '0'+'\t'+v

f1_out = open('DTBP_m','w')
f1_out.write("#name\tfirst\tsecond\n")
for k,v in n_dic.items():
	f1_out.write(k+'\t'+v+'\n')
f1_out.close()
print 'done'


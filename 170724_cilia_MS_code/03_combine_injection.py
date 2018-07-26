f1 = open('tsv/p11.tsv.logSpecE_hit_list_best','r')
f2 = open('tsv/p12.tsv.logSpecE_hit_list_best','r')
f3 = open('tsv/p13.tsv.logSpecE_hit_list_best','r')
f1.readline()
header = f1.next()
f1_dic =dict()
f2_dic =dict()
f3_dic =dict()

f_o = open('combine_injection','w')
f_o.write(header)

for line in f1:
	if not line.startswith('#'):
		f_o.write(line)
for line in f2:
	if not line.startswith('#'):	
		f_o.write(line)
for line in f3:
	if not line.startswith('#'):
		f_o.write(line)
f1.close()
f2.close()
f3.close()
f_o.close()

print 'done'

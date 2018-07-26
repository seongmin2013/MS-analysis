import sys
filename_txt = sys.argv[1]
f1 = open(filename_txt,'r')
f2 = open(filename_txt,'r')
nf1 = f1.name.replace('.logSpecE_hit_list_best','')
f1.readline()

f1_list = dict()
f2_list = dict()
n = 1
m = 1
err = 0

for line in f1:
	tokens = line.strip().split("\t")
	tmp_scan_num = tokens[0]
        tmp_e = float(tokens[7])
	if (tokens[5].split('_')[0] != 'XXX'):	
        	f1_list[tmp_scan_num] = float(tmp_e)
	else:
        	f2_list[tmp_scan_num] = float(tmp_e) 
f1.close()

sort_1 = sorted(f1_list.values())
sort_2 = sorted(f2_list.values())

while 1:
	if err > 0.05:
		tmp_real = dict((k,v) for k,v in f1_list.items() if v >= max_v)
		tmp_decoy = dict((k,v) for k,v in f2_list.items() if v >= max_v)
		f1_out = open("%s_FDR005.txt"%nf1,'w')
		f2_out = open("%s_FDR005_decoy.txt"%nf1,'w')
		tmp_line = f2.readline()
		f1_out.write(tmp_line)
		f2_out.write(tmp_line)
		for line in f2:
			tokens = line.strip().split("\t")
			tmp_scan_num = tokens[0]
			if(tmp_scan_num in tmp_real):
				f1_out.write(line)
			elif(tmp_scan_num in tmp_decoy):
				f2_out.write(line)
		print "FDR success"
		print err
		f1_out.close()
		f2_out.close()
		f2.close()
		break

	tmp_real = dict()
	tmp_decoy = dict()
	max_1 = sort_1[-n]
	max_2 = sort_2[-m]
	max_v = max(max_1,max_2)
	if max_v == max_2:
		m +=1
	else:
		n +=1
	tmp_real = list((v) for v in sort_1 if v >= max_v)
	real = len(tmp_real)
	tmp_decoy = list((v) for v in sort_2 if v >= max_v)
       	decoy = len(tmp_decoy)
	total = real+decoy
	err = decoy*1.0/total

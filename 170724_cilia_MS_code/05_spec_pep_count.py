import sys
filename_txt = sys.argv[1]
f1 = open(filename_txt,'r')
f1_name = f1.name.replace('_FDR001.txt','')
f1_name = f1_name.replace('_FDR005.txt','')
f1.readline()

f1_list = dict()
f1_list2 = dict()
for line in f1:
        tokens = line.strip().split("\t")
        if (not tokens[5] in f1_list):
            f1_list[tokens[5]] = 1
        else:
            f1_list[tokens[5]] += 1
	if (not tokens[4] in f1_list2):
            f1_list2[tokens[4]] = 1
        else:
            f1_list2[tokens[4]] += 1
f1.close()

import operator
f2_list = sorted(f1_list.items(), key=operator.itemgetter(1),reverse=True) 
f3_list = sorted(f1_list2.items(), key=operator.itemgetter(1),reverse=True) 

f1_out = open("%s_#Spectrum.txt"%f1_name,'w')
f1_out.write("#Spectrum_name\tnum\n")
for k,v in f2_list:
	f1_out.write(k+'\t'+str(v)+'\n')
f1_out.close()

f2_out = open("%s_#pepSpectrum.txt"%f1_name,'w')
f2_out.write("#pep_name\tnum\tnum\n")
for k,v in f3_list:
	f2_out.write(k+'\t'+str(v)+'\t'+str(v)+'\n')
f2_out.close()

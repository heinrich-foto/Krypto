# -*- coding: utf-8 -*- 
import math
import sys

def count(X,which):
	count=0
	for i in range(4):
		#print(i,which)
		if (X[i]==which):
			#print(i,count)
			count+=1
	return count	
	
def toBinary(n):
# https://stackoverflow.com/questions/699866/python-int-to-binary/20643178#20643178
#                                                Länge des jeweiligen Bit. zb 64 oder hier 8
    return ''.join(str(1 & int(n) >> i) for i in range(4)[::-1])

counter_null = 0
counter_eins = 0

for i in range(16):
	#print(i)
	binary = list(toBinary(i))
	count_null = count(binary,'0')
	count_eins = count(binary,'1')
	print("{0:3} {1}\t0={2:3} 1={3:3}".format(i,"".join(binary),count_null,count_eins))

	counter_null += count_null * (i+1)
	counter_eins += count_eins * (i+1)

print("\t\t0={0:3} 1={1:3}".format(counter_null,counter_eins))
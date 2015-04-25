# -*- coding: utf-8 -*- 
import math
import sys

def reverse(X):
# Man bildet das sogenannte Einerkomplement, 
# indem man jede Zahl durch ihr Gegenteil ersetzt, 
# also die 0 durch die 1 und die 1 durch die 0.
	for i in range(8):
		if (X[i]=='0'):
			X[i]='1'
		else:
			X[i]='0'
	return list(''.join(map(str,X)))	# gibt wieder eine Liste aus char zurück.

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(8)[::-1])

def rotate(X,r):
# alle bits werden von rechts nach link um r 
# Schritte verschoben.
	for i in range(int(r)):
		value = X.pop(0)
		X.append(value)
	return list(''.join(map(str,X))) 	# gibt wieder eine Liste aus char zurück.

def add(X,Y):
# Binäre Addition
	Z=['','','','','','','','']
	x=7
	carry=0
	while x >= 0:
		summe = (int(X[x])+int(Y[x])+carry)
		if (summe>1):
			carry=1
		else:
			carry=0
		Z[x]=(summe%2)
		x -= 1
	return list(''.join(map(str,Z)))	# gibt wieder eine Liste aus char zurück.

def sub(X,Y):
# Binäre Subtraktion
# http://www.ulthryvasse.de/subtraktion-von-binaeren-zahlen.html
	Z=['','','','','','','','']
	X=add(reverse(X),list(toBinary(1))) # An das Einerkomplement wird eine Eins addiert
	Z=add(X,Y)							# dies wird dann mit Y addiert.

	return list(''.join(map(str,Z)))	# gibt wieder eine Liste aus char zurück.

def xor(X,Y):
# Binäres XOR mit bereits implementiertem XOR operator.
	Z=['','','','','','','','']
	x=0
	while x < 8:
		Z[x]=(int(X[x])^int(Y[x]))
		x += 1
	return list(''.join(map(str,Z)))	# gibt wieder eine Liste aus char zurück.

n = 8
r = 1

count_a = 0
count_b = 0
count_c = 0
count_d = 0

Test_X = list(toBinary(10))
Test_Y = list(toBinary(90))
print(int(''.join(Test_X),2))
print(int(''.join(Test_Y),2))
print(int(''.join(map(str,add(Test_Y,Test_X))),2))
print()

Test_X = list(toBinary(10))
Test_Y = list(toBinary(4))
print(int(''.join(Test_X),2))
print(int(''.join(Test_Y),2))
print(int(''.join(map(str,sub(Test_Y,Test_X))),2))
print()

Test_X = list(toBinary(127))
Test_Y = list(toBinary(128))
print(int(''.join(Test_X),2))
print(int(''.join(Test_Y),2))
print(int(''.join(map(str,sub(Test_Y,Test_X))),2))

print(Test_X)
print(Test_Y)
print(sub(Test_Y,Test_X))
print()

Test_Z=list(toBinary(112))
print(int(''.join(Test_Z)))
print(reverse(Test_Z))


Test_X = list(toBinary(128))
Test_Y = list(toBinary(112))
print(int(''.join(Test_X),2))
print(int(''.join(Test_Y),2))
print(int(''.join(map(str,xor(Test_Y,Test_X))),2))

print(Test_X)
print(Test_Y)
print(xor(Test_Y,Test_X))

Test_X = list(toBinary(2))
Test_Y = list('11110000')
print(int(''.join(Test_X),2))
print(Test_X)
print(int(''.join(Test_Y),2))
print(Test_Y)
print(int(''.join(map(str,rotate(sub(Test_X,Test_Y),1))),2))
print(Test_X)
print(Test_Y)
print(rotate(sub(Test_X,Test_Y),1))

print()
Test_X = list(toBinary(253))
Test_Y = list(toBinary(2))
print(int(''.join(Test_X),2))
print(Test_X)
print(int(''.join(Test_Y),2))
print(Test_Y)
print(int(''.join(map(str,add(Test_X,Test_Y))),2))

print(add(Test_X,Test_Y))

#exit() # tests

for j in range(int(math.pow(2, n))):
	X=list(toBinary(j))
	Y=list('11110000')

	# Aufgabe A
	exp_a = rotate(xor(X,Y),r)
	exp_b = xor(rotate(X,r),rotate(Y,r))
	if (exp_a==exp_b):
		count_a += 1
	#	print("A: ({0:3} xor {1:3}) << == ({0:3} <<) xor ({1:3} <<) \t {2:3}=={3:3}".format( int(''.join(X),2), int(''.join(Y),2), int(''.join(exp_a),2), int(''.join(exp_b),2)))
	#	print("A: {0} {1} \t {2} \t {3}=={4}\t {5}".format(''.join(X), ''.join(Y),count_a,exp_a,exp_b,j))
	
	#Aufgabe D
	X=list(toBinary(j))
	Y=list('10100101')

	exp_a = rotate(sub(X,Y),r)
	exp_b = sub(rotate(X,r),rotate(Y,r))
	if (exp_a==exp_b):
		count_d += 1
	#	print("D: {0} {1} \t {2} \t {3}=={4}\t {5}".format(''.join(X), ''.join(Y),count_d,exp_a,exp_b,j))
	#else:
	#	print("D: {0} {1} \t {2} \t {3}!={4}\t {5}".format(''.join(X), ''.join(Y),count_a,exp_a,exp_b,j))
	
	for i in range(int(math.pow(2,n))):
		#Aufgbae B
		Z=list('00000001')
		X=list(toBinary(j))
		Y=list(toBinary(i))

		exp_a = add(Y,xor(X,Z))
		exp_b = xor(add(X,Y),add(Z,Y))
		if (exp_a==exp_b):
			count_b += 1
		#	print("B: ({0:3} xor {1:3}) add {4:2} == ({0:3} add {4:3}) xor ({1:3} add {4:3}) \t {2:3}=={3:3}".format( int(''.join(X),2), int(''.join(Z),2), int(''.join(exp_a),2), int(''.join(exp_b),2), int(''.join(Y),2)))
		#	print("B: {0} {1} \t {2} \t {3}=={4}\t {5},{6}".format(''.join(X), ''.join(Y),count_b,exp_a,exp_b,j,i))
		#else:
		#	print("B: ({0:3} xor {1:3}) add {4:2} == ({0:3} add {4:3}) xor ({1:3} add {4:3}) \t {2:3}=={3:3}".format( int(''.join(X),2), int(''.join(Z),2), int(''.join(exp_a),2), int(''.join(exp_b),2), int(''.join(Y),2)))
		#	print("B: {0} {1} \t {2} \t {3}!={4}\t {5},{6}".format(''.join(X), ''.join(Y),count_b,exp_a,exp_b,j,i))
		
		#Aufgabe C
		Z=list('10000000')
		X=list(toBinary(j))
		Y=list(toBinary(i))

		exp_a = add(Y,xor(X,Z))
		exp_b = xor(add(X,Y),add(Z,Y))
		if (exp_a==exp_b):
			count_c += 1
		#	print("C: {0} {1} \t {2} \t {3}=={4}\t {5},{6}".format(''.join(X), ''.join(Y),count_c,exp_a,exp_b,j,i))
power_a = math.pow(2,n)
power_b = math.pow(2,n)*power_a
print("a) {0}\t b) {1}\t c) {2}\t d) {3}".format(count_a//power_a*100,count_b//power_b*100,count_c//power_b*100,count_d//power_a*100))
print("a) {0}\t b) {1}\t c) {2}\t d) {3}".format(count_a,count_b,count_c,count_d))
import sys
from math import sqrt


seive = [False,False] + [True]*(1000000-1)
seive[2*2::2] = [False]*((1000000//2)-1)
for i in range(3,int(sqrt(1000000))+1,2):
	for j in range(i,(1000000//i)+1):
		seive[i*j] = False
res = [k for k in range(1000000+1) if seive[k]]
while True:
	n = int(input())
	if n == 0:
		break
	
	Bool = True
	for i in res:
		if seive[n-i]:
			print(str(n) + ' = ' + str(i) +' + '+str(n-i))
			Bool = False
			break
	if Bool:
		print("Goldbach's conjecture is wrong.")

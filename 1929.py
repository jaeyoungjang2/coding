import sys
from math import sqrt
prime_lst = list(map(int,sys.stdin.readline().rstrip().split()))
res_set = set()
for i in range(2,prime_lst[1]+1):
	res_set.add(i)

mi_set = set()
for i in range(2, int(sqrt(prime_lst[1]))+1):
	index = prime_lst[1]//i
	for j in range(i,index+1):
		mi_set.add(i*j)

res = sorted(res_set - mi_set)
for i in res:
	if i < prime_lst[0]:
		continue
	else:
		print(i)


import sys
from itertools import combinations, product

def cal_GCD(a,b):
	if b == 0:
		return a
	return cal_GCD(b,a%b)

res_lst = []
dist_lst = []
num = list(map(int,sys.stdin.readline().rstrip().split()))
Q_lst = list(map(int,sys.stdin.readline().rstrip().split()))

if len(Q_lst) == 1:
	print(abs(Q_lst[0]-num[1]))
else:
	comb_lst = product(Q_lst,[num[1]])
	for i in comb_lst:
		dist_lst.append(abs(i[1]-i[0]))
	#dist_comb = combinations(dist_lst,2)
	target = dist_lst.pop(0)
	while dist_lst:
		b = dist_lst.pop()
		target = cal_GCD(target,b)
	print(target)

	
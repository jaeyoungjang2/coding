import sys
from math import sqrt
count = sys.stdin.readline().rstrip()
count_lst = list(map(int,sys.stdin.readline().rstrip().split()))
res = 0
for i in count_lst:
	Bool = True
	if i < 2:
		continue
	for j in range(2,int(sqrt(i))+1):

		if i%j == 0:
			Bool = False
	if Bool:
		res += 1
print(res)

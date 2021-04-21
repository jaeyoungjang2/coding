import sys
cnt = int(sys.stdin.readline().rstrip())
target = [5,25,125]
res = 0
for i in target:
	res += cnt//i
print(res)



import sys
count_lst = list(map(int,sys.stdin.readline().rstrip().split()))
print(count_lst)
def cal_GCD(a,b):
	if b == 0:
		return(a)
	else:
		return(cal_GCD(b,a%b))

GCD = cal_GCD(count_lst[0],count_lst[1])
LCM = count_lst[0]*count_lst[1]/GCD
print(GCD)
print(int(LCM))
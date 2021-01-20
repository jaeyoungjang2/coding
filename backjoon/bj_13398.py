# 10
# 10 -4 3 1 5 6 -35 12 21 -1
import sys

cnt = int(input())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

for_d = [lst[0]]
for i in range(1,cnt):
    if for_d[i-1] > 0 :
        for_d.append(lst[i]+for_d[i-1])
    else:
        for_d.append(lst[i])


rev_lst = lst[::-1]
rev_d = [rev_lst[0]]

for i in range(1,cnt):
    if rev_d[i-1] > 0 :
        rev_d.append(rev_lst[i]+rev_d[i-1])
    else:
        rev_d.append(rev_lst[i])
rev_d = rev_d[::-1]

res = 0
for i in range(cnt-2):
    temp = max(for_d[i] + rev_d[i+2], for_d[i], rev_d[i])
    if res < temp:
        res = temp


print(max(res,for_d[-1],for_d[-2],rev_d[-1],rev_d[-2]))
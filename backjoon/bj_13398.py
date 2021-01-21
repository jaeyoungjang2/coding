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

res = -1001
for i in range(1,cnt-1):
    temp = max(for_d[i-1] + rev_d[i+1], for_d[i])
    if res < temp:
        res = temp

print(max(for_d[0],for_d[-1],res))
# 10
# 1 5 2 1 4 3 4 5 2 1

import sys
cnt = int(input())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

in_d = [1]*cnt
de_d = [1]*cnt

for i in range(1,cnt):
    for j in range(0,i):
        if lst[i] > lst[j] and in_d[j] >= in_d[i]:
            in_d[i] = in_d[j] + 1

for i in range(cnt-2, -1,-1):
    for j in range(cnt-1,i,-1):
        if lst[i] > lst[j] and de_d[j] >= de_d[i]:
            de_d[i] = de_d[j] + 1

res = 0
for i in range(cnt):
    if res < de_d[i] + in_d[i]:
        res = de_d[i] + in_d[i]
print(res-1)





import sys
cnt = int(input())
d = [1] * cnt
lst = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(1,cnt):
    for j in range(0,i):
        if d[i] <= d[j] and lst[i] < lst[j]:
            d[i] = d[j] + 1

print(max(d))
        
    
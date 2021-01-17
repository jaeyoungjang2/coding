import sys
n = int(input())
lst = list(map(int,sys.stdin.readline().rstrip().split()))
d = [0] * n

for idx, i in enumerate(lst):
    
    for j in range(idx):
        if d[j] > d[idx] and lst[j] < lst[idx]:
            d[idx] = d[j]
    d[idx] += i
        
print(max(d))

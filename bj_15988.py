lst = [0,1,2,4,7]+ [0]*9999996

for i in range(5,1000001):
    lst[i] = (lst[i-1]+lst[i-2]+lst[i-3])%1000000009
c = int(input())
for i in range(c):
    n = int(input())
    print(lst[n])


#n = 3
#26 40 83
#49 60 57
#13 89 99
import sys
n = int(input())
res = list(map(int,sys.stdin.readline().rstrip().split()))
print(res)
for _ in range(n-1):
    lst = list(map(int,sys.stdin.readline().rstrip().split()))
    res0 = min(res[1],res[2])+lst[0]
    res1 = min(res[0],res[2])+lst[1]
    res2 = min(res[0],res[1])+lst[2]
    res[0] = res0
    res[1] = res1
    res[2] = res2
    print(res)

print(min(res))
    


        

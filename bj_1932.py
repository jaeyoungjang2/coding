import sys 

n = int(input())
lst = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    lst.append(temp)
    if i == 0:
        continue
    else:
        for j in range(0,i+1):
            if j == 0:
                lst[i][0] += lst[i-1][0]
            elif j == i:
                lst[i][j] += lst[i-1][j-1]
            else:
                lst[i][j] += max(lst[i-1][j-1],lst[i-1][j])

print(max(lst[-1]))



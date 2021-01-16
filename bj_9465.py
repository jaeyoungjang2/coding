import sys
cnt = int(input())

for _ in range(cnt):
    lst = [[],[]]
    n = int(input())
    lst[0] = list(map(int,sys.stdin.readline().rstrip().split()))
    lst[1] = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(1,n):
        if i >= 2:
            lst[0][i] = max(lst[1][i-1],lst[0][i-2],lst[1][i-2]) + lst[0][i]
            lst[1][i] = max(lst[0][i-1],lst[1][i-2],lst[0][i-2]) + lst[1][i]
        else:
            lst[0][1] = lst[1][0] + lst[0][1]
            lst[1][1] = lst[0][0] + lst[1][1]
    print(max(lst[0][-1],lst[1][-1]))
import sys

count = int(input())
for i in range(count):
    y_lst = []
    lst = list(map(int,sys.stdin.readline().strip().split()))
    N = lst[0]
    M = lst[1]
    x = lst[2]
    y = lst[3]
    lc = 1
    temp_y = (x + N)%M
    if x==y and x < N and y < M:
        print(x)
        continue
    while True:        
        if temp_y == y:
            print((lc*N)+x)
            break
        elif temp_y in y_lst:
            print(-1)
            break
        lc += 1
        y_lst.append(temp_y)
        temp_y = (temp_y + N)%M


import sys
lst = list(map(int,sys.stdin.readline().strip().split()))
N = lst[0]
M = lst[1]

a = []
for i in range(N):
    a.append(list(map(int,sys.stdin.readline().strip().split())))

res = 0
for i in range(N):
    for j in range(M):
        if j+3 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
            if temp > res : res = temp
        if i+3 < N:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if temp > res : res = temp
        if i+1 < N and j+2 < M:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            if temp > res : res = temp
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
            if temp > res : res = temp
        if i+1 < N and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            if temp > res : res = temp
        if i+2 < N and j -1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
            if temp > res : res = temp
        if i-1 >= 0 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
            if temp > res : res = temp
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            if temp > res : res = temp
        if i+1 < N and j+2 < M:            
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
            if temp > res : res = temp
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            if temp > res : res = temp
        if i+1 < N and j+1 < M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            if temp > res : res = temp
        if i-1 >= 0 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
            if temp > res : res = temp
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            if temp > res : res = temp
        if i+1 < N and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            if temp > res : res = temp
        if i+2 < N and j-1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            if temp > res : res = temp
        if i-1 >= 0 and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+1]
            if temp > res : res = temp
        if i+1 < N and j+2 < M:
            temp = a[i][j] + a[i][j+1] + a[i][j+2]  + a[i+1][j+1]
            if temp > res : res = temp
        if i+2 < N and j+1 < M:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j+1]
            if temp > res : res = temp
        if i+2 < N and j-1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j-1]
            if temp > res : res = temp

print(res)
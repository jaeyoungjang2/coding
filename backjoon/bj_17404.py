import sys

cnt = int(input())
lst = [[0]*3 for _ in range(cnt)]
for i in range(cnt):
    lst[i] = list(map(int,sys.stdin.readline().rstrip().split()))

res = [[0]*3 for _ in range(cnt)]
result = []
for start_color in ['r','g','b']:
    for idx, i in enumerate(lst):
        if idx == 0 and start_color == 'r':
            res[0] = [i[0],1001,1001]
        elif idx == 0 and start_color == 'g':
            res[0] = [1001,i[1],1001]
        elif idx == 0 and start_color == 'b':
            res[0] = [1001,1001,i[2]]
        else:
            res[idx][0] = min(res[idx-1][1],res[idx-1][2]) + i[0]
            res[idx][1] = min(res[idx-1][0],res[idx-1][2]) + i[1]
            res[idx][2] = min(res[idx-1][0],res[idx-1][1]) + i[2]
    
    if start_color == 'r':
        result.append(min(res[-1][1],res[-1][2]))
    elif start_color == 'g':
        result.append(min(res[-1][0],res[-1][2]))
    elif start_color == 'b':
        result.append(min(res[-1][0],res[-1][1]))


print(min(result))
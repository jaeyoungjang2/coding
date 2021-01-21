cnt = int(input())

lst = [[0]*3 for _ in range(cnt+1)]
lst[1] = [1,1,1]
for i in range(2,cnt+1):
    temp = lst[i-1][1] + lst[i-1][2]
    lst[i][0] = temp
    lst[i][1] = sum(lst[i-1])
    lst[i][2] = temp

print(sum(lst[cnt])%9901)
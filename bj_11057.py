lst = [[0]*10 for _ in range(1001)]
lst[1] = [1,1,1,1,1,1,1,1,1,1]

cnt = int(input())
for i in range(2,cnt+1):
    for j in range(10):
        lst[i][j] = sum(lst[i-1][:j+1])%10007


print(sum(lst[cnt])%10007)
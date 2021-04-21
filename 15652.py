import sys
n, m = list(map(int,sys.stdin.readline().split()))
lst = list(map(int,sys.stdin.readline().split()))
check = [False]*(n+1)
a = [0]*m
lst = sorted(lst)
def go(index, n, m):
    if index == m:
        for i in range(m):            
            print(lst[a[i]-1], end=' ')
            # print(a[i], end=' ')
        print()
        return

    # 첫번째 숫자
    for i in range(1,n+1):
        if check[i]:
            continue
        # 사용한 숫자 저장
        a[index] = i
        check[i] = True
        go(index+1,n,m)
        check[i] = False
go(0,n,m)
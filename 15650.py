import sys
n, m = list(map(int,sys.stdin.readline().split()))
check = [False]*(n+1)
a = [0]*m

def go(index,start, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return

    # 첫번째 숫자
    for i in range(start,n+1):
        if check[i]:
            continue
        # 사용한 숫자 저장
        check[i] = True
        a[index] = i
        
        go(index+1,i+1,n,m)
        
        check[i] = False

go(0,1,n,m)
import sys
n, m = list(map(int,sys.stdin.readline().split()))
a = [0]*m

def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return

    # 첫번째 숫자
    for i in range(1,n+1):        
        # 사용한 숫자 저장
        a[index] = i
        go(index+1,n,m)
go(0,n,m)
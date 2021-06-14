import sys


def cal(n, m, x, y):
    dic = {}
    count = 0
    if x == y:
        return x
    while True:
        total = n*count+x
        targetY = (n*count+x) % m
        if targetY == 0:
            targetY = m
        if targetY == y:
            return total

        if (x, targetY) in dic:
            return -1
        dic[x, targetY] = 0

        count += 1


def main():
    count = int(input())
    for i in range(count):
        N, M, X, Y = list(map(int, sys.stdin.readline().split()))
        res = cal(N, M, X, Y)
        print(res)


main()

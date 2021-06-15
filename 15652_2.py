n, m = map(int, input().split())
res = []


def cal(stand):
    if len(res) == m:
        for i in res:
            print(i, end=' ')
        print()
        return
    for i in range(stand, n+1):
        res.append(i)
        cal(i)


cal(1)

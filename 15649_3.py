n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    dic[i] = True
res = []


def cal(res):
    if len(res) == m:
        for i in res:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        if dic[i]:
            res.append(i)
            dic[i] = False
            cal(res)
            res.pop()
            dic[i] = True


cal(res)

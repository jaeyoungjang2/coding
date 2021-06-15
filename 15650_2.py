n, m = map(int, input().split())
lst = [0] * n
res = []

for i in range(n):
    lst[i] = i+1


def cal(index):
    if len(res) == m:
        for i in res:
            print(i, end=' ')
        print()
        return
    if index >= n:
        return
    res.append(lst[index])
    cal(index+1)
    res.pop()
    cal(index+1)


cal(0)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

dic = {}
resdic = {}
res = [0]*m
for i in lst:
    dic[i] = True


def cal(index, target):
    if index == m:
        if tuple(res) not in resdic:
            for i in res:
                print(i, end=' ')
            print()
            resdic[tuple(res)] = 0
        return
    if target >= n:
        return
    i = lst[target]
    res[index] = i
    cal(index+1, target+1)
    cal(index, target+1)


cal(0, 0)

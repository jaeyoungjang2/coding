n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

dic = {}
res = [0]*m
for i in lst:
    dic[i] = True


def cal(index):
    if index == m:
        for i in res:
            print(i, end=' ')
        print()
        return
    for i in lst:
        if dic[i]:
            res[index] = i
            dic[i] = False
            cal(index+1)
            dic[i] = True


cal(0)

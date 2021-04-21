L, C = input().strip().split()
lst = input().strip().split()
resLst = []
dic = {}

for i in lst:
    dic[i] = True


def check(res):
    checkCount = 0
    checkLst = ["a", "e", "i", "o", "u"]
    for i in res:
        if i in checkLst:
            checkCount += 1
    if checkCount == 2:
        return True
    return False


def go(res):
    if len(res) == int(L):
        if check(res):
            resLst.append(res)
        return
    lst = list(dic.keys())
    print(lst)
    for i in lst:
        if dic[i]:
            dic[i] = False
            go(res + i)
            dic[i] = True


go("")
resLst.sort()
print(resLst)

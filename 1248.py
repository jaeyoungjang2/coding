count = int(input())
string = input()
res = []
dic = {}


index = 0
for i in range(count):
    for j in range(i, count):
        try:
            dic[i][j] = string[index]
        except:
            dic[i] = {}
            dic[i][j] = string[index]
        index += 1


def check(res, j):
    print(res)
    for i in range(j):
        total = sum(res[i : j + 1])
        if dic[i][j] == "+" and total < 0:
            return False
        elif dic[i][j] == "-" and total > 0:
            return False
        elif dic[i][j] == 0 and totla != 0:
            return False
    return True


def go(index, res, i, j):
    if j == count:
        i += 1
        j = i
    elif j != count:
        j += 1

    if j == count:
        return res

    if dic[j][j] == 0:
        res.append(0)
        check(res, j)
        go(index + 1, res, i, j)
    elif dic[j][j] == "+":
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            res.append(int(i))
            check(res, j)
            go(index + 1, res, i, j)
    elif dic[j][j] == "-":
        for i in [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]:
            res.append(int(i))
            check(res, j)
            go(index + 1, res, i, j)
    return res


print(go(0, res, -1, -1))

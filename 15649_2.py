N, finish = map(int, input().split())


def add(lst, res, count):
    # global finish
    if len(res) == finish:
        print(res)
    if count == finish:
        return
    for i in lst:
        if i in res:
            continue
        res.append(i)
        add(lst, res, count+1)
        res.pop()
        add(lst, res, count+1)


def main(N):
    count = 0
    res = []
    lst = []
    for i in range(1, N+1):
        lst.append(i)

    add(lst, res, count)


main(N)

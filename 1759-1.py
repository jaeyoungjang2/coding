n, m = map(int, input().split())
passwd_lst = list(input().split())
passwd_lst.sort()


def go(passwdLst, targetLength, index, currPasswd):
    # print(currPasswd + "\t" + str(index))
    if len(currPasswd) == targetLength:
        print(currPasswd)
        return
    if index == len(passwdLst):
        return
    go(passwd_lst, targetLength, index + 1, currPasswd + passwdLst[index])
    go(passwd_lst, targetLength, index + 1, currPasswd)


go(passwd_lst, n, 0, "")

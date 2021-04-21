import sys

n, m = map(int, input().split())
a = input().split()
a.sort()


def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in "aeiou":
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(n, alpha, password, index):

    if len(password) == n:
        if check(password):
            print(password)
        return
    if index == len(alpha):
        return
    go(n, alpha, password + alpha[index], index + 1)
    go(n, alpha, password, index + 1)


go(n, a, "", 0)

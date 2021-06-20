lst = [55, 1765, 98, 44432, 3298]


def check(num):

    strNum = str(num)
    length = len(strNum)
    for i in range(1, length):
        if strNum[i-1] == strNum[i]:
            return False
    return True


for i in lst:
    # 문제시작
    i = i+1
    while True:
        if check(i):
            result = i
            break
        i += 1
    print(i)


# 제출
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def nameCheck(name):
    if name.endswith('pdf') or name.endswith('xls') or name.endswith('doc'):
        return True
    return False


def permCheck(perm):
    if perm[0] == 'r' and perm[1] == '-':
        return True
    return False


def solution(S):
    # write your code in Python 3.6
    minNameLength = len(S)
    for i in S.split('\n'):
        owner, perm, name = i.strip().split()
        if owner == 'root' and nameCheck(name) and permCheck(perm):
            if minNameLength > len(name):
                minNameLength = len(name)
    if minNameLength == len(S):
        return "NO FILES"
    else:
        return(str(minNameLength))

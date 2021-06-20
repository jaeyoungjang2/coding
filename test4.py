S = '  root r-x delete-this.xls'


def nameCheck(name):
    if name.endswith('pdf') or name.endswith('xls') or name.endswith('doc'):
        return True
    return False


def permCheck(perm):
    if perm[0] == 'r' and perm[1] == '-':
        return True
    return False


minNameLength = len(S)
for i in S.split('\n'):

    i = i.strip()
    resLst = []
    owner, perm, name = i.split()
    print(i)

    if owner == 'root' and nameCheck(name) and permCheck(perm):
        if minNameLength > len(name):
            minNameLength = len(name)
        print("HI")
    print()
if minNameLength == len(S):
    print("NO FILES")
else:
    print(str(minNameLength))

# 제출
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def check(num):
    # 동일한 수가 연속해서 나오는지 확인해주는 함수
    strNum = str(num)
    length = len(strNum)
    for i in range(1, length):
        if strNum[i-1] == strNum[i]:
            # 동일한 수가 연속해서 나올 시 False 를 return
            return False
    # 동일한 수가 연속해서 나오지 않을 경우 True를 return
    return True


def solution(N):
    # write your code in Python 3.6
    N = N+1
    while True:
        # 동일한 수가 연속해서 나오지 않을 경우만 while문 종료
        if check(N):
            break
        N += 1
    return(N)

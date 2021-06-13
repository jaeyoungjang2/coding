import sys
num = int(input())
count = int(input())
exceptLst = list(map(str, sys.stdin.readline().split()))

res = abs(100 - num)
plusNum = num
minusNum = num
channel = num


def check(lst, num):
    for i in str(num):
        if i in lst:
            return False
    return True


while True:
    if min(abs(plusNum - num), abs(minusNum - num)) > res:
        channel = num + res + 1
        break
    if check(exceptLst, minusNum) and minusNum >= 0:
        channel = minusNum
        break
    elif check(exceptLst, plusNum) and plusNum <= 1000000:
        channel = plusNum
        break
    minusNum -= 1
    plusNum += 1

if res > abs(channel - num) + len(str(channel)):
    res = abs(channel - num) + len(str(channel))
print(res)

import sys
N, M = list(map(int, sys.stdin.readline().split()))
lst = [[0]*N for i in range(M)]

for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))


def type1(lst, N, M):
    # 가로 4개 막대기
    maxNum = 0
    # ㅁㅁㅁㅁ
    for i in range(N):
        for j in range(M-3):
            tempNum = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i][j+3]
            if tempNum > maxNum:
                maxNum = tempNum
    # ㅁ
    # ㅁ
    # ㅁ
    # ㅁ
    for i in range(N-3):
        for j in range(M):
            tempNum = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+3][j]
            if tempNum > maxNum:
                maxNum = tempNum
    return maxNum


def type2(lst, N, M):
    # ㅁ
    # ㅁ
    # ㅁㅁ
    maxNum = 0
    # 세로
    for i in range(N-2):
        # 가로
        for j in range(M-1):
            tempNum = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+2][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
            #  ㅁ
            #  ㅁ
            # ㅁㅁ
            tempNum = lst[i+2][j] + lst[i+2][j+1] + lst[i+1][j+1] + lst[i][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁㅁ
            # ㅁ
            # ㅁ
            tempNum = lst[i][j] + lst[i][j+1] + lst[i+1][j] + lst[i+2][j]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁㅁ
            #  ㅁ
            #  ㅁ
            tempNum = lst[i][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i+2][j+1]
            if tempNum > maxNum:
                maxNum = tempNum

    #   ㅁ
    # ㅁㅁㅁ
    for i in range(N-1):
        for j in range(M-2):
            tempNum = lst[i+1][j] + lst[i+1][j+1] + lst[i+1][j+2] + lst[i][j+2]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁ
            # ㅁㅁㅁ
            tempNum = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+1][j+2]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁㅁㅁ
            #   ㅁ
            tempNum = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j+2]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁㅁㅁ
            # ㅁ
            tempNum = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j]
            if tempNum > maxNum:
                maxNum = tempNum

    return maxNum


def type3(lst, N, M):
    # ㅁㅁ
    # ㅁㅁ
    maxNum = 0
    for i in range(N-1):
        for j in range(M-1):
            tempNum = lst[i][j] + lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
    return maxNum


def type4(lst, N, M):
    # ㅁ
    # ㅁㅁ
    #  ㅁ
    maxNum = 0
    for i in range(N-2):
        for j in range(M-1):
            tempNum = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
            #  ㅁ
            # ㅁㅁ
            # ㅁ
            tempNum = lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j]
            if tempNum > maxNum:
                maxNum = tempNum
    # ㅁㅁ
    #  ㅁㅁ
    for i in range(N-1):
        for j in range(M-2):
            tempNum = lst[i][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i+1][j+2]
            if tempNum > maxNum:
                maxNum = tempNum
            #  ㅁㅁ
            # ㅁㅁ
            tempNum = lst[i][j+1] + lst[i][j+2] + lst[i+1][j] + lst[i+1][j+1]
            if tempNum > maxNum:
                maxNum = tempNum

    return maxNum


def type5(lst, N, M):
    # ㅁ
    # ㅁㅁ
    # ㅁ
    maxNum = 0
    for i in range(N-2):
        for j in range(M-1):
            tempNum = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+1][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
            #  ㅁ
            # ㅁㅁ
            #  ㅁ
            tempNum = lst[i][j+1] + lst[i+1][j+1] + lst[i+2][j+1] + lst[i+1][j]
            if tempNum > maxNum:
                maxNum = tempNum

    #  ㅁ
    # ㅁㅁㅁ
    for i in range(N-1):
        for j in range(M-2):
            tempNum = lst[i+1][j] + lst[i+1][j+1] + lst[i+1][j+2] + lst[i][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
            # ㅁㅁㅁ
            #  ㅁ
            tempNum = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j+1]
            if tempNum > maxNum:
                maxNum = tempNum
    return maxNum


res = max([
    type1(lst, N, M),
    type2(lst, N, M),
    type3(lst, N, M),
    type4(lst, N, M),
    type5(lst, N, M)
])
print(res)

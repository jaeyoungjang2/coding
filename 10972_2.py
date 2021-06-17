n = int(input())
lst = list(map(int, input().split()))


def next_permutation(lst):
    lstSize = len(lst)
    targetIndex = -1

    target = lst[lstSize-1]
    for index in range(lstSize-2, -1, -1):
        if lst[index] > target:
            target = lst[index]
        else:
            targetIndex = index
            break

    if targetIndex == -1:
        return -1

    compare = lst[targetIndex+1]
    compareIndex = targetIndex + 1

    for i in range(targetIndex+2, len(lst)):
        if lst[targetIndex] < lst[i] < compare:
            compare = lst[i]
            compareIndex = i
    lst[compareIndex], lst[targetIndex] = lst[targetIndex], lst[compareIndex]

    lst[targetIndex+1:] = reversed(lst[targetIndex+1:])

    res = ' '.join(list(map(str, lst)))
    return res


res = next_permutation(lst)
print(res)

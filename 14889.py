count = int(input())
dic = {}
res = 0
for i in range(count):
    lst = list(map(int, (input().split())))
    for j, value in enumerate(lst):
        try:
            dic[i][j] = value
            res += value
        except:
            dic[i] = {}
            dic[i][j] = value
            res += value


def check(firstTeam, secondTeam):
    firstTeamValue = 0
    secondTeamValue = 0
    for i in firstTeam:
        for j in firstTeam:
            firstTeamValue += dic[i][j]
    for i in secondTeam:
        for j in secondTeam:
            secondTeamValue += dic[i][j]
    temp = firstTeamValue - secondTeamValue
    if temp < 0:
        temp = -temp
    return temp


def go(index, firstTeam, secondTeam):
    global res
    if len(firstTeam) > count / 2 or len(secondTeam) > count / 2:
        return
    if len(firstTeam) == count / 2 and len(secondTeam) == count / 2:
        temp = check(firstTeam, secondTeam)
        res = min(res, temp)
        return
    go(index + 1, firstTeam + [index], secondTeam)
    go(index + 1, firstTeam, secondTeam + [index])


go(0, [], [])
print(res)
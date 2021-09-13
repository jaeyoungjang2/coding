def calculateScore(userA_score, userB_score):
    userA_totalScore = 0
    userB_totalScore = 0
    scoreInfo = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    for i in range(len(info)):
        if userA_score[i] >= userB_score[i]:
            userA_totalScore += info[i] * scoreInfo[i]
            continue
        userB_totalScore += info[i] * scoreInfo[i]

    return userB_totalScore > userA_totalScore


info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
n = 5

res = []
for i in info:
    if i < n:
        res.append(i + 1)
        n -= i + 1
        continue
    res.append(0)

print(res)

while True:
    resTemp = []
    for i in res:
        resTemp.append(i)

    index = resTemp.index(max(resTemp))
    print(index)
    if index == 10:
        break
    print("HI")
    newN = max(resTemp)
    resTemp[index] = 0
    for i in range(index + 1, 11):
        if info[i] > resTemp[i] and info[i] < newN + resTemp[i]:
            newN -= (info[i] + 1 - resTemp[i])
            resTemp[i] = info[i] + 1
    print(resTemp)
    if calculateScore(info, resTemp) == False:
        break
    res = resTemp
    print(res)

print(res)

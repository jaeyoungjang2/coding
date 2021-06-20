(S, C) = ('John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example')
print(C.lower())
naemDict = {}
resLst = []

for name in S.split('; '):
    nameType = name.split()
    if len(nameType) == 2:
        firstName = nameType[0].lower()
        lastName = nameType[1].lower()
    elif len(nameType) == 3:
        firstName = nameType[0].lower()
        middleName = nameType[1].lower()
        lastName = nameType[2].lower()

    tempLastName = ''
    for i in lastName:
        if i != '-':
            tempLastName += i
    lastName = tempLastName

    emailPrefix = firstName+'.'+lastName[:8]

    try:
        naemDict[emailPrefix] += 1
    except:
        naemDict[emailPrefix] = 1

    if naemDict[emailPrefix] == 1:
        email = '{emailPrefix}.{C}.com'.format(
            emailPrefix=emailPrefix, C=C.lower())
    else:
        email = '{emailPrefix}{count}.{C}.com'.format(
            emailPrefix=emailPrefix, C=C.lower(), count=naemDict[emailPrefix])
    resLst.append(email)
print('; '.join(resLst))


# 제출
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    naemDict = {}
    resLst = []

    for name in S.split('; '):
        nameType = name.split()
        # middle name이 존재하는 경우
        if len(nameType) == 2:
            firstName = nameType[0].lower()
            lastName = nameType[1].lower()
        # middle name이 존재하지 않는 경우
        elif len(nameType) == 3:
            firstName = nameType[0].lower()
            middleName = nameType[1].lower()
            lastName = nameType[2].lower()

        # 하이픈이 있을때 제외하고 진행
        tempLastName = ''
        for i in lastName:
            if i != '-':
                tempLastName += i
        lastName = tempLastName

        emailPrefix = firstName+'.'+lastName[:8]

        # first name , last name 중복이 있을 경우
        # 중복 개수 확인
        try:
            naemDict[emailPrefix] += 1
        except:
            naemDict[emailPrefix] = 1

        # 중복이 있을 경우와 없을 경우 output 생성
        if naemDict[emailPrefix] == 1:
            email = '{emailPrefix}@{C}.com'.format(
                emailPrefix=emailPrefix, C=C.lower())
        else:
            email = '{emailPrefix}{count}@{C}.com'.format(
                emailPrefix=emailPrefix, C=C.lower(), count=naemDict[emailPrefix])
        # 샘플별 결과 저장
        resLst.append(email)

    # result format으로 변경
    res = '; '.join(resLst)
    return res

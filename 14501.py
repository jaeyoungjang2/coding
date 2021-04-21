dDay = int(input())
dayList, payList = [0], [0]
for _ in range(dDay):
    day, pay = list(map(int, input().split()))
    dayList.append(day)
    payList.append(pay)

ans = 0


def go(day, pay):
    global ans
    if dDay + 1 == day:
        ans = max(ans, pay)
        return
    if dDay + 1 < day:
        return
    go(day + 1, pay)
    go(day + dayList[day], pay + payList[day])


go(1, 0)
print(ans)

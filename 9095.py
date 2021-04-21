def cal(sum, goal):
    if sum > goal:
        return 0
    elif sum == goal:
        return 1
    now = 0
    for i in range(1,4):
        now += cal(sum+i,goal)
    return now


count = int(input())
for i in range(count):
    target = int(input())
    print(cal(0,target))
    
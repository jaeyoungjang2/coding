e, v = list(map(int, input().split()))
# lstGraph 선언
lstGraph = [[] for i in range(e)]
visit = [False for i in range(e)]
res = False

# edge, vertex의 수를 받음
for i in range(v):
    a, b = list(map(int, input().split()))
    lstGraph[a].append(b)
    lstGraph[b].append(a)

# 재귀함수 선언


def go(target, depth, lst):
    global res
    if depth >= 4:
        res = True
        return
    for i in lstGraph[target]:
        if visit[i] == False:
            visit[i] = True
            go(i, depth+1, lst)
            visit[i] = False


for i in range(e):
    visit[i] = True
    go(i, 0, visit)
    visit[i] = False

print(1 if res else 0)

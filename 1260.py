e, v, start = map(int, input().split())

graph = [[] for i in range(e+1)]
visit = [False for i in range(e+1)]

for i in range(v):
    a, b = map(int, input().split())
    graph[a] = b
    graph[b] = a

def go(visit, target, depth,DFS):
    if depth >= e:
        DFS_res = True
        return
    for i in graph[target]:
        if visit[i] == False:
            visit[i] = True
            go(visit, i, depth+1)


visit[0] = True
visit[1] = True
DFS = [1]
DFS_res = False
BFS = [1]
go(visit,1,0,DFS))
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
visit = [False for i in range(n + 1)]

visit[0] = True

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a+1].append(b+1)
    graph[b+1].append(a+1)

def dfs(graph, i, myDepth):
    global ans
    visit[i] = True
    
    if myDepth >= 4:
        ans = True
        return
    for j in graph[i]:
        if visit[j] == False:
            dfs(graph, j, (myDepth+1))
            visit[j] = False
        
        

ans = False
for i in range(1, n+1, 1):
    dfs(graph, i, 0)
    visit[i] = False
    if ans:
        break

print(1 if ans else 0)
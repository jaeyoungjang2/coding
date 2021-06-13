import sys
N, M, V = list(map(int, sys.stdin.readline().split()))
# asd

lst = [[] for _ in range(N+1)]
stackLst = [V]
queueLst = [V]
vDic = {}
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    vDic[a] = vDic[b] = False
    if a not in lst[b]:
        lst[b].append(a)

    if b not in lst[a]:
        lst[a].append(b)

for i in range(len(lst)):
    lst[i].sort()

# def dfs(stack, order, lst):
#     if len(stack) == 0:
#         print(' '.join(map(str, order)))
#         return
#     if len(lst[stack[-1]]) == 0:
#         stack.pop()
#         dfs(stack, order, lst)
#         return
#     target = lst[stack[-1]].pop(0)
#     if target not in order:
#         stack.append(target)
#         order.append(target)
#         dfs(stack, order, lst)
#     elif target in order:
#         if len(lst[stack[-1]]) == 0:
#             stack.pop()
#         dfs(stack, order, lst)


def dfs(v):
    print(v, end=' ')
    vDic[v] = True
    for i in lst[v]:
        if vDic[i] == False:
            dfs(i)


# def bfs(queue, order, lst):
#     if len(queue) == 0:
#         print(' '.join(map(str, order)))
#         return
#     if len(lst[queue[-1]]) == 0:
#         queue.pop(0)
#         bfs(queue, order, lst)
#         return
#     targetLst = lst[queue.pop(0)]
#     for i in targetLst:
#         if i not in order:
#             queue.append(i)
#             order.append(i)
#     bfs(queue, order, lst)

def bfs(v):
    vDic[v] = False
    queue = [v]
    print(v, end=" ")
    while queue:
        target = queue.pop(0)
        for i in lst[target]:
            if vDic[i] == True:
                vDic[i] = False
                print(i, end=" ")
                queue.append(i)


dfsOrder = [V]
bfsOrder = [V]
# dfs(stackLst, dfsOrder, lst)
dfs(V)
print()
# bfs(queueLst, bfsOrder, bfslst)
bfs(V)
print()

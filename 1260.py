import sys
N, M, V = list(map(int, sys.stdin.readline().split()))


lst = [[] for _ in range(N+1)]
bfslst = [[] for _ in range(N+1)]
stackLst = [V]
queueLst = [V]

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    if a not in lst[b]:
        lst[b].append(a)
        bfslst[b].append(a)
    if b not in lst[a]:
        lst[a].append(b)
        bfslst[a].append(b)


def dfs(stack, order, lst):
    if len(stack) == 0:
        print(' '.join(map(str, order)))
        return
    if len(lst[stack[-1]]) == 0:
        stack.pop()
        dfs(stack, order, lst)
        return
    target = lst[stack[-1]].pop(0)
    if target not in order:
        stack.append(target)
        order.append(target)
        dfs(stack, order, lst)
    elif target in order:
        if len(lst[stack[-1]]) == 0:
            stack.pop()
        dfs(stack, order, lst)


def bfs(queue, order, lst):
    if len(queue) == 0:
        print(' '.join(map(str, order)))
        return
    if len(lst[queue[-1]]) == 0:
        queue.pop(0)
        bfs(queue, order, lst)
        return
    targetLst = lst[queue.pop(0)]
    for i in targetLst:
        if i not in order:
            queue.append(i)
            order.append(i)
    bfs(queue, order, lst)


dfsOrder = [V]
bfsOrder = [V]
dfs(stackLst, dfsOrder, lst)
bfs(queueLst, bfsOrder, bfslst)

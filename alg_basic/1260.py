from collections import deque
import sys
input = sys.stdin.readline


def dfs(node):
    if visited[node]:
        return
    visited[node] = True

    print(node, end=" ")
    for i in arr[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    visited = [False for _ in range(N+1)]
    visited[node] = True
    deq.append(node)

    while deq:
        x = deq.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)
        print(x, end=" ")   


N, V, M = map(int, input().split())
visited = [False for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
deq = deque()
for _ in range(V):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()


dfs(M)
print()
bfs(M)

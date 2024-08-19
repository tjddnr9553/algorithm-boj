import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global flag
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 0:
                deq.append((ny, nx))
                visited[ny][nx] = True
                if ny == n-1:
                    flag = True
                    break


deq = deque()
dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
flag = False

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(m):
    if graph[0][i] == 0:
        deq.append((0, i))
        visited[0][i] = True
        bfs()

if flag:
    print("YES")
else:
    print("NO")

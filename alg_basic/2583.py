from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    area = 1
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                deq.append((ny, nx))
                area += 1
    areas.append(area)

m, n, k = map(int, input().split())
rects = []
for _ in range(k):
    command = list(map(int, input().split()))
    rects.append((command))

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
deq = deque()
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
areas = []
for i in rects:
    for j in range(i[1], i[3]):
        for z in range(i[0], i[2]):
            graph[j][z] = 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            deq.append((i, j))
            bfs()

print(len(areas))
print(*sorted(areas))
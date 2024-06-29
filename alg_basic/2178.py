from collections import deque
import sys
input = sys.stdin.readline

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
y, x = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(y)]
deq = deque()


def bfs():
    while deq:
        yy, xx = deq.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < x and 0 <= ny < y and graph[ny][nx] == 1:
                graph[ny][nx] = graph[yy][xx]+graph[ny][nx]
                deq.append((ny, nx))


deq.append((0, 0))
bfs()
print(graph[y-1][x-1])

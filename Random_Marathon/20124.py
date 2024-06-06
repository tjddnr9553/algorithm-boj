import sys
input = sys.stdin.readline

n = int(input().strip())

arr = []
for _ in range(n):
    command = input().split()
    name = command[0]
    score = int(command[1])
    arr.append((score, name))

arr.sort(key=lambda x: (-x[0], x[1]))

print(arr[0][1])

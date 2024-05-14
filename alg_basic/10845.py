from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == "push":
        arr.append(command[1])
    elif command[0] == "pop":
        if len(arr) == 0:
            print("-1")
        else:
            print(arr.popleft())
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        if len(arr) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(arr) == 0:
            print("-1")
        else:
            print(arr[0])
    else:
        if len(arr) == 0:
            print("-1")
        else:
            print(arr[-1])

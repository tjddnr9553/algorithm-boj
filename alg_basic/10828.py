import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    arr = list(map(str, input().split()))

    if arr[0] == "push":
        stack.append(arr[1])
    elif arr[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif arr[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif arr[0] == "size":
        print(len(stack))
    elif arr[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

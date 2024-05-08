import sys
input = sys.stdin.readline

n = int(input())
temp = []
for _ in range(n):
    arr = list(map(str, input().strip()))
    flag = True
    answer = []

    for i in range(len(arr)):
        if arr[i] == "(":
            answer.append(arr[i])
        elif arr[i] == ")":
            if len(answer) == 0:
                flag = False
                break
            else:
                answer.pop()

    if len(answer) > 0:
        flag = False

    if flag == False:
        print("NO")
    else:
        print("YES")

import sys
input = sys.stdin.readline

bact = 1
n = int(input())
cost = list(map(int, input().split()))
answer = []

for i in range(n):
    if i == 0:
        bacteria = bact * 2 - cost[i]
        answer.append(bacteria)
    else:
        bacteria = answer[i-1] * 2 - cost[i]
        answer.append(bacteria)

if answer[n-1] >= 0:
    print(answer[n-1]%(10**9+7))
else:
    print("error")

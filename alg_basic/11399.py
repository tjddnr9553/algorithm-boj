import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
time = []

arr.sort()

for i in range(len(arr)):
    time.append(sum(arr[:i+1]))

print(sum(time))
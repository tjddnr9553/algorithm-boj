import sys
input = sys.stdin.readline
arr = []
idx = []
answer = 0
for i in range(8):
    arr.append(int(input()))

for i in range(5):
    max_idx = arr.index(max(arr))
    answer += arr[max_idx]
    arr[max_idx] = 0
    idx.append(max_idx+1)

idx.sort()
print(answer)
print(*idx)

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    arr = list(map(str, input().split()))
    
    temp = []
    for i in arr:
        temp.append(i[::-1])    # i[::-1] 뒤집어서 정렬
    print(*temp)

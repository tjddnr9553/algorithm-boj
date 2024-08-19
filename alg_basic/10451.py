import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(number):
    global count
    if visited[number] == True:
        count += 1
        return
    
    visited[number] = True
    dfs(mixed_permutation[number]-1)


T = int(input())

for _ in range(T):
    count = 0
    N = int(input())
    permutation = [i for i in range(1, N+1)]
    mixed_permutation = list(map(int, input().split()))
    visited = [False for _ in range(N)]

    for i in mixed_permutation:
        if visited[i-1] == False:
            dfs(i-1)
            
    print(count)

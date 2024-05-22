import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6
n = int(input())
dp = [0]*(n+1)


def fibo(num):
    if num <= 1:
        return 1
    if dp[num]:
        return dp[num]
    dp[num] = fibo(num-2)+fibo(num-1)
    return dp[num]


dp[n] = fibo(n) % 10007
print(dp[n])

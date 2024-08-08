import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):
    a, b = map(int, input().split())
    c = a+b
    print("Case #" + str(i) + ": "+str(a)+" + " + str(b)+" = " + str(c))

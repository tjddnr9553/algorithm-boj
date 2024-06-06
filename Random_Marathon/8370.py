import sys
input = sys.stdin.readline

arguments = list(map(int, input().split()))
print(arguments[0]*arguments[1] + arguments[2]*arguments[3])

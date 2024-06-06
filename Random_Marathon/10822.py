import sys
input = sys.stdin.readline

arguments = list(map(int, input().split(",")))
print(sum(arguments))
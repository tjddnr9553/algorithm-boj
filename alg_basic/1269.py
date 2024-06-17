import sys
input = sys.stdin.readline
x, y = map(int, input().split())
x_list = set(map(int, input().split()))
y_list = set(map(int, input().split()))
print(len(x_list ^ y_list))

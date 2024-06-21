import sys
input = sys.stdin.readline
num = []

for _ in range(3):
    num.append(int(input()))

first = num[0]+num[1]-num[2]
print(first)
second = int(str(num[0])+str(num[1])) - num[2]
print(second)

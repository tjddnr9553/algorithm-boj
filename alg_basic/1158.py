import sys
input = sys.stdin.readline

length, num = map(int, input().split())
arr = [i for i in range(1, length+1)]
temp = num - 1
result = []

while len(arr) > 0:
    temp %= len(arr)
    result.append(arr.pop(temp))
    temp += num - 1

print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")                         

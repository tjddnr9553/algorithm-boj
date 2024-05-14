import sys
from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))


# word = list(map(str, input().strip()))
# temp = []
# n = int(input())
# cursor = len(word)

# for _ in range(n):
#     command = list(map(str, input().split()))
#     if command[0] == "P":
#         word.append(command[1])
#         cursor += 1
#     elif command[0] == "L" and cursor > 0:
#         temp.append(word.pop())
#         cursor -= 1
#     elif command[0] == "D" and cursor < len(word) and len(temp) > 0:
#         word.append(temp.pop())
#         cursor += 1
#     elif command[0] == "B" and cursor > 0 and len(temp) > 0:
#         word.append(temp.pop())
#         word.pop()
#         word += temp
# temp = temp[::-1]

# if temp:
#     word += temp
# print(''.join(word))

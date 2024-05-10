import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
temp = []
n = int(input())
cursor = len(word)

for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == "P":
        word.append(command[1])
        cursor += 1
    elif command[0] == "L" and cursor > 0:
        temp.append(word.pop())
        cursor -= 1
    elif command[0] == "D" and cursor < len(word) and len(temp) > 0:
        word.append(temp.pop())
        cursor += 1
    elif command[0] == "B" and cursor > 0 and len(temp) > 0:
        word.append(temp.pop())
        word.pop()
        word += temp

    print("temp : ", temp)
temp = temp[::-1]

if temp:
    word += temp
print(''.join(word))

import sys
input = sys.stdin.readline

n = int(input())
word = input().strip()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = 0
temp = ""

for i in word:
    if i in num:
        temp += i
    else:
        if 0 < len(temp) < 7:
            answer += int(temp)
            temp = ""
            
if temp:
    answer += int(temp)

print(answer)

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
answer = [0]
flag = 1

for i in range(len(num)-1):
    if num[i] > num[i+1]:
        answer.append(1)
    else:
        answer.append(0)

sum_answer = sum(answer)

if sum_answer == 7:
    print("descending")
elif sum_answer == 0:
    print("ascending")
else:
    print("mixed")
    
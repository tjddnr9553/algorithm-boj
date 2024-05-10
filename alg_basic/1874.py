import sys
input = sys.stdin.readline

n = int(input())
num_list = []
result = []

for _ in range(n):
    num_list.append(int(input()))

stack = []
current = 1
idx = 0

for num in num_list:
    while current <= num:  # 현재 넣어야 하는 수까지 스택에 push
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:  # 스택의 top이 현재 수와 같다면 pop
        stack.pop()
        result.append('-')
    else:  # 스택의 top이 현재 수와 다르다면 주어진 수열을 만들 수 없음
        print('NO')
        exit(0)

for r in result:
    print(r)


# n = int(input())
# num_list = []
# arr = []
# x = 1
# max_idx = 0
# flag = True
# for i in range(n):
#     num_list.append(int(input()))

# max_idx = num_list.index(max(num_list))

# for i in range(max_idx, n-1):
#     if num_list[i] < num_list[i+1]:
#         flag = False
#         break

# if flag == False:
#     print("NO")
# else:
#     for i in range(n*2):
#         if len(arr) == 0 and n == len(num_list):
#             arr.append(x)
#             print("+")
#             x += 1

#         if (len(num_list) == 0):
#             break

#         if arr[-1] == num_list[0] and len(arr) > 0:
#             arr.pop()
#             print("-")
#             num_list.pop(0)
#         else:
#             arr.append(x)
#             print("+")
#             x += 1

import sys
input = sys.stdin.readline

n = int(input())
stack_front = []
stack_back = []


def move_front_list():
    if not stack_front and stack_back:
        while stack_back:
            stack_front.append(stack_back.pop())


def move_back_list():
    if not stack_back and stack_front:
        while stack_front:
            stack_back.append(stack_front.pop())


for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == "push_back":
        stack_back.append(command[1])
    elif command[0] == "push_front":
        stack_front.append(command[1])
    elif command[0] == "pop_front":
        if len(stack_front)+len(stack_back) == 0:
            print("-1")
        elif len(stack_front) == 0:
            move_front_list()
            print(stack_front.pop())
        else:
            print(stack_front.pop())
    elif command[0] == "pop_back":
        if len(stack_front)+len(stack_back) == 0:
            print("-1")
        elif len(stack_back) == 0:
            move_back_list()
            print(stack_back.pop())
        else:
            print(stack_back.pop())
    elif command[0] == "size":
        print(len(stack_front)+len(stack_back))
    elif command[0] == "empty":
        if len(stack_front)+len(stack_back) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if len(stack_front)+len(stack_back) == 0:
            print("-1")
        elif len(stack_front) == 0:
            print(stack_back[0])
        else:
            print(stack_front[-1])
    elif command[0] == "back":
        if len(stack_front)+len(stack_back) == 0:
            print("-1")
        elif len(stack_back) == 0:
            print(stack_front[0])
        else:
            print(stack_back[-1])

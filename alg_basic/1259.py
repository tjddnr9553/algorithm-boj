import sys

input = sys.stdin.readline
flag = True

while True:
    word = input().strip()
    reverse_word = word[::-1]
    if word == reverse_word:
        flag = True
    else:
        flag = False    

    if word == "0":
        break
    
    if flag:
        print("yes")
    else:
        print("no")

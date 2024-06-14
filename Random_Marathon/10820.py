import sys

while True:
    answer = [0, 0, 0, 0]
    words = sys.stdin.readline().rstrip('\n')

    if not words:
        break

    for i in range(len(words)):
        if words[i].isdigit():
            answer[2] += 1
        elif words[i].isupper():
            answer[1] += 1
        elif words[i].islower():
            answer[0] += 1
        elif words[i].isspace():
            answer[3] += 1
    print(answer, sep=" ")

import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
for i in range(97, 123):
    print(word.count(chr(i)), end=" ")

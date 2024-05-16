import sys
input = sys.stdin.readline
result = []


def reverse_word():
    temp = []
    i = 0
    while i < len(word):
        if word[i] == "<":
            while word[i] != ">":
                result.append(word[i])
                i += 1
        elif word[i].isalnum():  # isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴
            start = i
            while i < len(word) and word[i].isalnum():
                i += 1
            temp = word[start:i]
            temp = temp[::-1]
            result.append(temp)
        else:
            result.append(word[i])
            i += 1


word = input().strip()
reverse_word()
print("".join(result))

# import sys
# input = sys.stdin.readline


# def reverse_words(s):
#     result = []
#     i = 0
#     while i < len(s):
#         if s[i] == '<':
#             while s[i] != '>':
#                 result.append(s[i])
#                 i += 1
#             result.append(s[i])
#             i += 1
#         elif s[i].isalnum():
#             start = i
#             while i < len(s) and s[i].isalnum():
#                 i += 1
#             word = s[start:i]
#             result.append(word[::-1])
#         else:
#             result.append(s[i])
#             i += 1
#     return ''.join(result)


# s = input().strip()
# print(reverse_words(s))

import sys
input = sys.stdin.readline

a_1, a_2, a_3 = map(int, input().split())
c_1, c_2, c_3 = map(int, input().split())
b_1 = c_1-a_3
b_2 = int(c_2/a_2)
b_3 = c_3-a_1

print(b_1,b_2,b_3,sep=" ")
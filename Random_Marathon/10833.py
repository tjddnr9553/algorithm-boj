import sys
input = sys.stdin.readline

remains = 0
for _ in range(int(input())):
    students, apples = map(int,input().split())
    remains += apples % students
    
print(remains)

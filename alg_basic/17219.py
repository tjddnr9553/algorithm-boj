import sys
input = sys.stdin.readline
dict = {}
n, m = map(int, input().split())
for _ in range(n):
    addr, id = map(str, input().split())
    dict[addr] = id

for _ in range(m):
    input_addr = input().strip()
    print(dict[input_addr])

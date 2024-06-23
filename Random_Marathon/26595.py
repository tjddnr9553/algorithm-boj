import sys
input = sys.stdin.readline

n = int(input())
a, a_cost, b, b_cost = map(int, input().split())
a_power = a*(n/a_cost)
b_power = b*(n/b_cost)
if a_power > b_power:
    print()

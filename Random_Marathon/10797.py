import sys
input = sys.stdin.readline

n = int(input())
cars = list(map(int, input().split()))

print(cars.count(n))
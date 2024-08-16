import sys
input = sys.stdin.readline

X = input().strip()
if X[0] == "0" and X[1] != "x":
    print(int(X, 8))
elif X[:2] == "0x":
    print(int(X, 16))
else:
    print(X)

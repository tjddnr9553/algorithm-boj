import sys
input = sys.stdin.readline

width = [0, 1, 1]
height = [0, 1, 2]

n = int(input())
for i in range(3, n+1):
    if i % 2 == 0:
        height.append(width[i-1]+height[i-1])
        width.append(width[i-1])
    else:
        width.append(width[i-1]+height[i-1])
        height.append(height[i-1])

print(2*(width[n]+height[n]))

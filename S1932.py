import sys

n = int(sys.stdin.readline())
triangle = [[int(sys.stdin.readline().rstrip())]]
for _ in range(n-1):
    up_stair = triangle.pop()
    triangle.append(list(map(int, sys.stdin.readline().split())))
    for i in range(len(triangle[0])):
        if i == 0:
            triangle[0][i] += up_stair[i]
        elif i == len(triangle[0]) - 1:
            triangle[0][i] += up_stair[i-1]
        else:
            triangle[0][i] += max(up_stair[i-1], up_stair[i])

print(max(triangle[0]))
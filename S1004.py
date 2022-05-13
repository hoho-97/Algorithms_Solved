import math

case = int(input())

for i in range(case):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())

    galaxy = int(input())

    for j in range(galaxy):
        cx, cy, r = map(int, input().split())

        range1 = math.sqrt(pow(x1 - cx, 2) + pow(y1 - cy, 2))
        range2 = math.sqrt(pow(x2 - cx, 2) + pow(y2 - cy, 2))

        if range1 < r and range2 < r:
            pass
        elif range1 < r or range2 < r:
            ans += 1

    print(ans)
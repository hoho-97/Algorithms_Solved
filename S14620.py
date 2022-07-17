from sys import stdin as st
from itertools import combinations

n = int(st.readline())
garden_cost = [list(map(int, st.readline().split())) for _ in range(n)]
seed_points = [(x, y) for x in range(1, n-1) for y in range(1, n-1)]
dx, dy = [0, -1, 0, 1, 0], [0, 0, 1, 0, -1]
ans = 200 * 15

def isDeadFlower(s1, s2):
    if abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) <= 2:
        return True
    return False

for seed1, seed2, seed3 in combinations(seed_points, 3):
    if isDeadFlower(seed1, seed2) or isDeadFlower(seed2, seed3) or isDeadFlower(seed1, seed3):
        continue
    else:
        (x1, y1), (x2, y2), (x3, y3) = seed1, seed2, seed3

        price = 0

        for i in range(5):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            nx3, ny3 = x3 + dx[i], y3 + dy[i]

            price += garden_cost[nx1][ny1] + garden_cost[nx2][ny2] + garden_cost[nx3][ny3]

        if price < ans:
            ans = price

print(ans)
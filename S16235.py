from collections import deque
from sys import stdin as st

n, m, k = map(int, st.readline().split())
A = [list(map(int, st.readline().split())) for _ in range(n)]
field = [[deque([]) for i in range(n)] for j in range(n)]
energy = [[5] * n for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0

for _ in range(m):
    x, y, z = map(int, st.readline().split())
    field[x-1][y-1].append(z)

for _ in range(k):
    breed_trees = []
    energy_summer = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            tree_box = field[x][y]

            for __ in range(len(tree_box)):
                tree = tree_box.popleft()

                if tree <= energy[x][y]:
                    energy[x][y] -= tree
                    tree_box.append(tree + 1)

                    if (tree + 1) % 5 == 0:
                        breed_trees.append((x, y))
                else:
                    energy_summer[x][y] += tree // 2

    for x in range(n):
        for y in range(n):
            energy[x][y] += energy_summer[x][y] + A[x][y]

    for breed in breed_trees:
        x, y = breed
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                field[nx][ny].appendleft(1)

for i in range(n):
    for j in range(n):
        ans += len(field[i][j])

print(ans)
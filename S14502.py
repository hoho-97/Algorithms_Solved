from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
lab = [list(map(int, st.readline().split())) for _ in range(n)]
ans, safe_num = 0, 0
virus = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        if lab[x][y] == 2:
            virus.append((x, y))


def bfs(case):
    q = deque(virus)
    safe_count = 0
    while q:
        virusX, virusY = q.popleft()

        for i in range(4):
            nx, ny = virusX + dx[i], virusY + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if case[nx][ny] == 0:
                    case[nx][ny] = 2
                    q.append((nx, ny))

    for c in case:
        safe_count += c.count(0)

    return safe_count

for i in range(n * m - 2):
    for j in range(i + 1, n * m - 1):
        for k in range(j + 1, n * m):
            ix, iy = i // m, i % m
            jx, jy = j // m, j % m
            kx, ky = k // m, k % m

            if lab[ix][iy] == 0 and lab[jx][jy] == 0 and lab[kx][ky] == 0:
                case = [list(li) for li in lab]
                case[ix][iy], case[jx][jy], case[kx][ky] = 1, 1, 1
                safe_num = bfs(case)

            if safe_num > ans:
                ans = safe_num

print(ans)

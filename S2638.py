from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
cheese = [list(map(int, st.readline().split())) for _ in range(n)]
ans = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while True:
    flag = True
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                flag = False
    if flag:
        break

    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] >= 1:
                    cheese[nx][ny] += 1
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    for i in range(n):
        for j in range(m):
            if cheese[i][j] > 2:
                cheese[i][j] = 0
            if cheese[i][j] == 2:
                cheese[i][j] = 1
    ans += 1

print(ans)
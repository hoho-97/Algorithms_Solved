from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
war = [list(st.readline().rstrip()) for _ in range(m)]
ans = [0, 0]
visited = [[False] * n for _ in range(m)]
dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]

def bfs(startX, startY):
    q = deque([(startX, startY)])
    visited[startX][startY] = True
    team_color = war[startX][startY]
    power = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and war[nx][ny] == team_color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        power += 1

    return power

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if war[i][j] == 'W':
                ans[0] += bfs(i, j) ** 2
            else:
                ans[1] += bfs(i, j) ** 2

print(*ans)
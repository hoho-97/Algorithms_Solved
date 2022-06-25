from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
pictures = [list(map(int, st.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans_num = 0
ans_max_size = 0


def bfs(startX, startY):
    q = deque([(startX, startY)])
    visited[startX][startY] = True
    picture_size = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and pictures[nx][ny] == 1:
                    picture_size += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return picture_size


for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1 and not visited[i][j]:
            ans_num += 1
            ans_max_size = max(ans_max_size, bfs(i, j))

print(ans_num)
print(ans_max_size)
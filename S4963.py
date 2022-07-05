from collections import deque
from sys import stdin as st

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, st.readline().split())
    ans = 0

    if w == 0 and h == 0:
        break

    field = [list(map(int, st.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and field[i][j] == 1:
                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < h and 0 <= ny < w:
                            if not visited[nx][ny] and field[nx][ny] == 1:
                                visited[nx][ny] = True
                                q.append((nx, ny))

                ans += 1

    print(ans)
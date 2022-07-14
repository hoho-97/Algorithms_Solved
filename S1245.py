from sys import stdin as st

n, m = map(int, st.readline().split())
field = [list(map(int, st.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0

def findTop(x, y):
    global flag

    visited[x][y] = True

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] > field[x][y]:
                flag = False
            if not visited[nx][ny]:
                if field[nx][ny] == field[x][y]:
                    findTop(nx, ny)

for i in range(n):
    for j in range(m):
        if field[i][j] > 0 and not visited[i][j]:
            flag = True

            findTop(i, j)

            if flag:
                ans += 1
print(ans)

import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

robot = (r, c)
clean = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

while True:
    (x, y) = robot
    if not clean[x][y]:
        clean[x][y] = True
        ans += 1
    for i in range(4):
        nx = x + dx[(d+3) % 4]
        ny = y + dy[(d+3) % 4]
        d = (d+3) % 4
        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] == 0 and not clean[nx][ny]:
                robot = (nx, ny)
                break

    if robot == (x, y):
        nx = x - dx[d]
        ny = y - dy[d]

        if field[nx][ny] == 1:
            break

        robot = (nx, ny)

print(ans)

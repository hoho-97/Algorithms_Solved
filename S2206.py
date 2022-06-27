from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
graph = [list(map(int, list(st.readline().rstrip()))) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for __ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1

while q:
    x, y, wall_break = q.popleft()

    if x == n-1 and y == m-1:
        print(visited[x][y][wall_break])
        exit(0)

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny][wall_break] == 0 and graph[nx][ny] == 0:
                q.append((nx, ny, wall_break))
                visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1

            if wall_break == 0 and graph[nx][ny] == 1:
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1

print(-1)
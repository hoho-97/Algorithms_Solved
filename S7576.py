from collections import deque
from sys import stdin as st

m, n = map(int, st.readline().split())
cage = []
start_tomatoes = []
empty = []
for i in range(n):
    line = list(map(int, st.readline().split()))
    for j, k in enumerate(line):
        if k == 1:
            start_tomatoes.append((i,j))
        elif k == -1:
            empty.append((i,j))
    cage.append(line)
visited = [[False for a in range(m)] for b in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    global visited, cage
    days = 0
    q = deque([start])

    while q[0]:
        tomatoes = q.popleft()
        next_tomatoes = []
        for (x, y) in tomatoes:
            visited[x][y] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and cage[nx][ny] == 0:
                        next_tomatoes.append((nx,ny))
                        cage[nx][ny] = 1

        q.append(next_tomatoes)
        days += 1
    for _ in range(len(empty)):
        x, y = empty.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if cage[nx][ny] == 0:
                    return -1

    return days-1

print(bfs(start_tomatoes))

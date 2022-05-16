import sys
from collections import deque

n = int(sys.stdin.readline())
danji = [list(map(int, sys.stdin.readline().rstrip())) for x in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []

#상하좌우 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(startX, startY):
    global danji, visited

    queue = deque([[startX, startY]])
    danji_num = 0

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        danji_num += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and danji[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    return danji_num

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and danji[i][j] != 0:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
for answer in ans:
    print(answer)
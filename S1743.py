import sys
from collections import deque

def bfs(field, p):
    queue = deque([p])
    result = 1
    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        field[x][y] = 0

        #좌
        if 1 <= x-1 <= n and 1 <= y <= m and field[x-1][y] != 0:
            field[x-1][y] = 0
            queue.append((x-1, y))
            result += 1
        #우
        if 1 <= x+1 <= n and 1 <= y <= m and field[x+1][y] != 0:
            field[x+1][y] = 0
            queue.append((x+1, y))
            result += 1
        #상
        if 1 <= x <= n and 1 <= y-1 <= m and field[x][y-1] != 0:
            field[x][y-1] = 0
            queue.append((x, y-1))
            result += 1
        #하
        if 1 <= x <= n and 1 <= y+1 <= m and field[x][y+1] != 0:
            field[x][y+1] = 0
            queue.append((x, y+1))
            result += 1
    return result

n, m, k = map(int, sys.stdin.readline().split())
ans = 0

field = [[0] * (m + 1) for _ in range(n+1)]
for i in range(k):
    row, col = map(int, sys.stdin.readline().split())
    field[row][col] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if field[i][j] == 1:
            result = bfs(field, (i, j))
            ans = max(ans, result)

print(ans)
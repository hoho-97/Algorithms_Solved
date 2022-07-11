from sys import stdin as st

r, c, k = map(int, st.readline().split())
graph = [list(st.readline().rstrip()) for _ in range(r)]
ans = [0] * (r*c+1)
visited = [[False] * c for _ in range(r)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def findWay(x, y, count):
    global visited, ans

    if x == 0 and y == c-1:
        ans[count] += 1
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and graph[nx][ny] != 'T':
                visited[nx][ny] = True
                findWay(nx, ny, count+1)
                visited[nx][ny] = False

visited[r-1][0] = True
findWay(r-1, 0, 1)
print(ans[k])
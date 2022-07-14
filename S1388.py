from sys import stdin as st

n, m = map(int, st.readline().split())

room = [list(st.readline().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0

def horizontal(x, y):
    global ans, visited

    if y >= m:
        ans += 1
        return

    if room[x][y] == '-':
        horizontal(x, y+1)
        visited[x][y] = True
    else:
        ans += 1
        return

def vertical(x, y):
    global ans, visited

    if x >= n:
        ans += 1
        return

    if room[x][y] == '|':
        visited[x][y] = True
        vertical(x+1, y)
    else:
        ans += 1
        return

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            if room[x][y] == '-':
                horizontal(x, y)
            else:
                vertical(x, y)

print(ans)
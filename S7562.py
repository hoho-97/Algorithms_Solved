from collections import deque
from sys import stdin as st

t = int(st.readline())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    l = int(st.readline())
    visited = [[False] * l for __ in range(l)]
    startX, startY = map(int, st.readline().split())
    destX, destY = map(int, st.readline().split())
    count = -1
    found = False
    q = deque([[(startX, startY)]])
    visited[startX][startY] = True

    while True:
        if found:
            print(count)
            break

        q_list = q.popleft()
        next_list = []

        for x, y in q_list:
            if x == destX and y == destY:
                found = True
                break

            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < l and 0 <= ny < l:
                    if not visited[nx][ny]:
                        next_list.append((nx, ny))
                        visited[nx][ny] = True

        q.append(next_list)
        count += 1
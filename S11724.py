import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
connected = [list() for _ in range(n+1)]
ans = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    connected[u].append(v)
    connected[v].append(u)

visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True

        while queue:
            v = queue.popleft()
            visited[v] = True

            for j in connected[v]:
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)

        ans += 1


print(ans)

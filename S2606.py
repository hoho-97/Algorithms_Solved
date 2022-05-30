from collections import deque
from sys import stdin as st

n, e = int(st.readline()), int(st.readline())
network = list([0] * n for _ in range(n))
ans = 0

for i in range(e):
    n1, n2 = map(int, st.readline().split())
    network[n1 - 1][n2 - 1], network[n2 - 1][n1 - 1] = 1, 1

q = deque([0])
visited = [True] + [False] * (n - 1)

while q:
    v = q.popleft()

    for node, connected in enumerate(network[v]):
        if connected == 1 and not visited[node]:
            q.append(node)
            visited[node] = True
            ans += 1

print(ans)
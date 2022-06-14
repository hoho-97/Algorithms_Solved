from collections import deque
from sys import stdin as st

bfs_ans = []
dfs_ans = []

def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        v = q.popleft()
        bfs_ans.append(v)

        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


def dfs(start, visited):
    visited[start] = True
    dfs_ans.append(start)
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited)


n, m, v = map(int, st.readline().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, st.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()


visited=[False] * (n + 1)
dfs(v, visited)
bfs(v)
print(" ".join(str(i) for i in dfs_ans))
print(" ".join(str(i) for i in bfs_ans))

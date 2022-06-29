from collections import deque
from sys import stdin as st

n, m = map(int, st.readline().split())
visited = [-1] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, st.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

q = deque([1])
visited[1] = 0

while q:
    v = q.popleft()

    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + 1
            q.append(i)

range = max(visited)
print(visited.index(range), range, visited.count(range))
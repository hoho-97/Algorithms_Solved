import math
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
ans = 0
MAX_V = math.pow(10, 5)

queue = deque([n])
visited = [0] * int(MAX_V + 1)

while queue:
    v = queue.popleft()

    if v == k:
        break

    for x in [v-1, v+1, v*2]:
        if 0 <= x and x <= MAX_V and not visited[x]:
            visited[x] = visited[v] + 1
            queue.append(x)

print(visited[k])
import math
import sys
from collections import deque

n = int(sys.stdin.readline())
MAX = int(math.pow(10, 6))

def bfs(n):
    queue = deque([1])
    visited = [0] * (MAX + 1)
    while queue:
        v = queue.popleft()

        if v == n:
            break

        for i in [v + 1, v * 2, v * 3]:
            if 1 <= i <= MAX:
                if visited[i] == 0:
                    visited[i] = visited[v] + 1
                    queue.append(i)
    return visited[n]


print(bfs(n))

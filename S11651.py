from sys import stdin as st

n = int(st.readline())
point = [tuple(map(int, st.readline().split())) for _ in range(n)]
point.sort(key=lambda x: (x[1],x[0]))
for p in point:
    print(p[0], p[1])
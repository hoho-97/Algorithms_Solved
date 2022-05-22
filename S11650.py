from sys import stdin as st

n = int(st.readline())
p = [tuple(map(int, st.readline().split())) for _ in range(n)]
p.sort(key=lambda x: (x[0],x[1]))
for i in range(n):
    print(p[i][0], p[i][1])

from sys import stdin as st

n = int(st.readline())
arr = [list(map(int, st.readline().split())) for _ in range(n)]

a = [1,2,3,4]
b = [1,2]
print(a.remove(b))
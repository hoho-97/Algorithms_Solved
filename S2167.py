from sys import stdin as st

n, m = map(int, st.readline().split())
arr = [list(map(int, st.readline().split())) for _ in range(n)]
k = int(st.readline())
sum = 0
for row in range(n):
    for col in range(m):
        sum += arr[row][col]
        arr[row][col] = sum

for _ in range(k):
    i, j, x, y = map(int, st.readline().split())

from sys import stdin as st

n = int(st.readline())
a = list(map(int, st.readline().split()))
b = list(map(int, st.readline().split()))
ans = 0

a.sort()
b.sort(reverse=True)

for i in range(n):
    ans += a[i] * b[i]

print(ans)
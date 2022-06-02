from sys import stdin as st

n, k = map(int, st.readline().split())
coin = []
ans = 0
for _ in range(n):
    coin.append(int(st.readline()))

for _ in range(n):
    value = coin.pop()
    ans += k // value
    k %= value

print(ans)
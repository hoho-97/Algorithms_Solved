from sys import stdin as st

h, w = map(int, st.readline().split())
blocks = list(map(int, st.readline().split()))
ans = 0
for i in range(1, w-1):
    left, right = max(blocks[:i]), max(blocks[i+1:])

    rain = min(left, right) - blocks[i]

    if rain > 0:
       ans += rain

print(ans)
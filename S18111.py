from sys import stdin as st

n, m, b = map(int, st.readline().split())
ground = [list(map(int, st.readline().split())) for _ in range(n)]
ans, ans_h = 6.4 * 10 ** 7, 0
secs = 0
for h in range(257):
    remove_blocks, put_blocks = 0, 0
    secs = 0
    inventory = b
    for i in range(n):
        for j in range(m):
            height = ground[i][j]
            if height < h:
                put_blocks += h - height
            elif height > h:
                remove_blocks += height - h
                inventory += height - h
    if put_blocks > inventory:
        continue
    secs = put_blocks + remove_blocks * 2
    if ans >= secs:
        ans = secs
        ans_h = h
print(ans, ans_h)
from sys import stdin as st

n = int(st.readline())
meetings = [tuple(map(int, st.readline().split())) for _ in range(n)]
ans = 0

meetings.sort(key=lambda x : (x[1], x[0]))
last_end = 0
for start, end in meetings:
    if start >= last_end:
        last_end = end
        ans += 1
print(ans)

from sys import stdin as st

n = int(st.readline())
atm = list(map(int, st.readline().split()))
atm.sort()
ans = 0

for i in range(n):
    ans += sum(atm[0:i+1])

print(ans)
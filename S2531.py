from sys import stdin as st

n, d, k, c = map(int, st.readline().split())

susi = [int(st.readline()) for _ in range(n)]
susi.extend(susi[:k-1])
min_diversity = k
ans = 0
for i in range(n):
    case = set(susi[i:i+k])
    case.add(c)

    ans = max(ans, len(case))
print(ans)
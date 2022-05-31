from sys import stdin as st

n = int(st.readline())
arr = list(map(int, st.readline().split()))
rank = sorted(list(set(arr)))
rank = {rank[i] : i for i in range(len(rank))}

for a in arr:
    print(rank[a], end=' ')
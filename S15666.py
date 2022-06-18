from itertools import combinations_with_replacement
from sys import stdin as st

n, m = map(int, st.readline().split())
nums = sorted(list(set(map(int, st.readline().split()))))

for case in combinations_with_replacement(nums, m):
    print(" ".join(map(str, case)))
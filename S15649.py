import sys
from sys import stdin as st

sys.setrecursionlimit(100)
n, m = map(int, st.readline().split())
numbers = [[x for x in range(1, n+1)] for _ in range(m)]

def dfs(case, position):
    new_case = case.copy()
    if position == m:
        for x in case:
            print(x, end=' ')
        print()
        return
    for num in numbers[position]:
        if position == 0:
            new_case = [num]
            dfs(new_case, position+1)
        if num not in new_case:
            new_case.append(num)
            dfs(new_case, position+1)
        new_case = case.copy()

dfs([], 0)

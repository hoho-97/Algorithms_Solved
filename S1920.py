import sys
from sys import stdin as st

sys.setrecursionlimit(100)
n = int(st.readline())
nodes = list(map(int, st.readline().split()))
nodes.sort()
m = int(st.readline())
search_numbers = list(map(int, st.readline().split()))

def searchTree(num, start_index, end_index):
    if start_index > end_index:
        return 0
    mid_index = (start_index + end_index) // 2
    if nodes[mid_index] == num:
        return 1
    elif nodes[mid_index] > num:
        return searchTree(num, start_index, mid_index - 1)
    else:
        return searchTree(num, mid_index + 1, end_index)


for search_number in search_numbers:
    print(searchTree(search_number, 0, n-1))



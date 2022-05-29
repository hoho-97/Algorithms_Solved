from sys import stdin as st

t = int(st.readline())
arr = [(1, 0), (0, 1)]

for i in range(2, 41):
    arr.append(((arr[i-2][0] + arr[i-1][0]), (arr[i-2][1] + arr[i-1][1])))

for _ in range(t):
    n = int(st.readline())
    print(arr[n][0], arr[n][1])
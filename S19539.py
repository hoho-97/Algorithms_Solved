from sys import stdin as st

n = int(st.readline())
h = list(map(int, st.readline().split()))
count_two = 0
if sum(h) % 3 != 0:
    print('NO')
else:
    for tree in h:
        count_two += tree // 2

    if count_two >= sum(h) // 3:
        print('YES')
    else:
        print('NO')
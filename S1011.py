from sys import stdin as st

case = int(st.readline())

for _ in range(case):
    x, y = map(int, st.readline().split())
    count, i = 1, 1
    num = (y-1) - (x+1)
    while True:
        if num < 0:
            print(count)
            break
        if count % 2 == 0:
            i += 1
        num -= i
        count += 1
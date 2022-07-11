from sys import stdin as st

while True:
    n, m = map(int, st.readline().split())

    if n == 0 and m == 0:
        break

    if n <= m and m % n == 0:
        print('factor')
    elif n > m and n % m == 0:
        print('multiple')
    else:
        print('neither')
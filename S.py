from math import sqrt
from sys import stdin as st

n = int(st.readline())
ans = n
for m in range(int(sqrt(n)), 0, -1):
    num = n
    count = 0
    for i in range(m, 0, -1):
        while num >= i ** 2:
            num -= i ** 2
            count += 1
    ans = min(ans, count)

print(ans)
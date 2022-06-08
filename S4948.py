from sys import stdin as st

prime = [False, False] + [True] * (123456 * 2)

for num in range(2, 123456 * 2 + 1):
    if prime[num]:
        for p in range(num * 2, 123456 * 2 + 1, num):
            prime[p] = False

while True:
    n = int(st.readline())
    prime_count = 0

    if n == 0:
        break

    print(prime[n+1:2 * n + 1].count(True))

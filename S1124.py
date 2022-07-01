import math
from sys import stdin as st

a, b = map(int, st.readline().split())
ans = 0
is_prime = [False, False] + [True] * (10 ** 5 - 1)

for i in range(2, 10**5 + 1):
    if is_prime[i]:
        for j in range(i*2, 10**5 + 1, i):
            is_prime[j] = False

def is_underprime(n):
    num = n
    primes_count = 0
    for i in range(2, int(math.sqrt(num))+1):
        if is_prime[i]:
            while True:
                if num % i != 0:
                    break
                num //= i
                primes_count += 1
        if num == 1:
            break
    if is_prime[num]:
        primes_count += 1

    return is_prime[primes_count]


for n in range(a, b+1):
    if is_underprime(n):
        ans += 1

print(ans)
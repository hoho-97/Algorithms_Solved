m, n = map(int, input().split())
prime_list = [False, False] + [True] * (n-1)
for i in range(2, n+1):
    if prime_list[i]:
        for j in range(i*2, n+1, i):
            prime_list[j] = False

for i in range(m, n+1):
    if prime_list[i]:
        print(i)
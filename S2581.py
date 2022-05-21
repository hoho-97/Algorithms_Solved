m = int(input())
n = int(input())
is_prime = [False, False] + [True for i in range(n-1)]
for i in range(2, n+1):
    if is_prime[i]:
        for j in range(i+i,n+1,i):
            is_prime[j] = False

prime = []
for num in range(m, n+1):
    if is_prime[num]:
        prime.append(num)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)
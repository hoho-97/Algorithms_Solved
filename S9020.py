import sys

case = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(case)]
n = max(nums)
is_prime = [False, False] + [True] * (n-1)
for i in range(2, n+1):
    if is_prime[i]:
        for j in range(i+i, n+1, i):
            is_prime[j] = False
for num in nums:
    num1 = int(num/2)
    num2 = int(num/2)
    for n2 in range(num2, num):
        if is_prime[n2] and is_prime[num1]:
            print('%d %d' % (num1, n2))
            break
        num1 -= 1
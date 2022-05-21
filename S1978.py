n = int(input())
nums = list(map(int, input().split()))
ans = 0

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in nums:
    if isPrime(num):
        ans += 1

print(ans)
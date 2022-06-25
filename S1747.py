import math

n = int(input())

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

while True:
    if isPrime(n) and isPalindrome(n):
        print(n)
        break

    n += 1
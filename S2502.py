import sys

d, k = map(int, input().split())

sys.setrecursionlimit(30)


def fibo_first(n):
    if n == 3:
        return 1
    elif n == 4:
        return 1
    else:
        return fibo_first(n - 1) + fibo_first(n - 2)


def fibo_second(n):
    if n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        return fibo_second(n - 1) + fibo_second(n - 2)


fibo_a = fibo_first(d)
fibo_b = fibo_second(d)
a = 0
while True:
    a += 1
    b = a

    while True:
        dduk = fibo_a * a + fibo_b * b
        if dduk == k:
            print(a)
            print(b)
            exit(0)
        elif dduk > k:
            break
        b += 1
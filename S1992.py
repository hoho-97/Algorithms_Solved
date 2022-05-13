import sys

sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
quad = [sys.stdin.readline().rstrip() for _ in range(n)]


def zip(quad, n):
    ans = ''
    count0, count1 = 0, 0
    for line in quad:
        count0 += line.count("0")
        count1 += line.count("1")
    if count0 == 0:
        return '1'
    elif count1 == 0:
        return '0'
    else:
        ans += '('
        arr = quad[0:n//2]
        ans += zip(list(map(lambda x: x[0:n//2], arr)), n//2)
        ans += zip(list(map(lambda x: x[n//2:n], arr)), n//2)
        arr = quad[n//2:n]
        ans += zip(list(map(lambda x: x[0:n//2], arr)), n//2)
        ans += zip(list(map(lambda x: x[n//2:n], arr)), n//2)
        ans += ')'
        return ans


print(zip(quad, n))
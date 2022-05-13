import sys

N, r, c = map(int, sys.stdin.readline().split())
ans = 0

while N > 1:
    N -= 1

    half = 2 ** N
    if r < half and c < half:
        ans += 0
    elif r < half and c >= half:
        ans += half * half
        c -= half
    elif r >= half and c < half:
        ans += half * half * 2
        r -= half
    elif r >= half and c >= half:
        ans += half * half * 3
        r -= half
        c -= half

if r == 0 and c == 1:
    ans += 1
elif r == 1 and c == 0:
    ans += 2
elif r == 1 and c == 1:
    ans += 3

print(ans)
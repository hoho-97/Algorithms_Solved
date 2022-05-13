n, l = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()

num = 0
ans = 0
for i in range(n):
    if pipe[i] > num:
        num = pipe[i] + l - 1
        ans += 1

print(ans)
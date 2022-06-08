n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def comb(start, size):
    global ans
    if len(sub_arr) == size:
        if sum(sub_arr) == s:
            ans += 1
        return

    for i in range(start, n):
        sub_arr.append(arr[i])
        comb(i + 1, size)
        sub_arr.pop()

for i in range(1,n+1):
    sub_arr = []
    comb(0, i)

print(ans)

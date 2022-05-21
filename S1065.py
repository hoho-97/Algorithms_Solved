n = int(input())
ans = 0
for i in range(1, n+1):
    if 1 <= i < 100:
        ans += 1
    elif 100 <= i <= 1000:
        if int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
            ans += 1
print(ans)
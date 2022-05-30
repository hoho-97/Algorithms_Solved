num = [1, 2]
n = int(input())
for i in range(2, n):
    num.append((num[i-2]+num[i-1])%10007)
print(num[n-1])
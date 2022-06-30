n = int(input())
numbers = [1] * 10
total, temp = 0, 0
for _ in range(n-1):
    total = sum(numbers)

    for i in range(10):
        if i != 0:
            total -= temp
        temp = numbers[i]
        numbers[i] = total

ans = sum(numbers)
print(ans%10007)
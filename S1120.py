a, b = input().split()

num = 50
for i in range(len(b) - len(a) + 1):
    difference = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            difference += 1
    num = min(num, difference)
print(num)
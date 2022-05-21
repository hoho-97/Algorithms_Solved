num = [True] * 11000
for i in range(1, 10000):
    n = i
    for j in str(i):
        n += int(j)
    num[n] = False
for i, n in enumerate(num[1:]):
    if i > 10000:
        break
    if n:
        print(i+1)
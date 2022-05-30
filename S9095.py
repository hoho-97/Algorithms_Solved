t = int(input())
sol = [1, 2, 4]
for i in range(3, 10):
    sol.append(sol[i-1] + sol[i-2] + sol[i-3])
for _ in range(t):
    print(sol[int(input()) - 1])


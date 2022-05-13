import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
li = [0] * n

li[0] = nums[0]
for x in range(1, n):
    li[x] = max(nums[x] + li[x-1], nums[x])

print(max(li))

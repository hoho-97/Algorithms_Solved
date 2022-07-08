from sys import stdin as st

nums = list(st.readline().split('-'))
for idx, num in enumerate(nums):
    ns = list(map(int, num.split('+')))
    if len(ns) > 1:
        nums[idx] = sum(ns)
nums = list(map(int, nums))
ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]
print(ans)


from collections import deque
from sys import stdin as st

n = int(st.readline())
numbers = deque([i for i in range(1,n+1)])
stack = [0]
ans = []
can_make = True
for i in range(n):
    input_num = int(st.readline())

    while stack[-1] != input_num:
        if not numbers:
            can_make = False
            break

        stack.append(numbers.popleft())
        ans.append('+')

    stack.pop()
    ans.append('-')

if can_make:
    for a in ans:
        print(a)
else:
    print('NO')
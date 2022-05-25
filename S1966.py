from collections import deque
from sys import stdin as st

t = int(st.readline())

for _ in range(t):
    n, m = map(int, st.readline().split())
    print_list = deque(enumerate(list(map(int, st.readline().split()))))
    priority_list = [0] * 10
    ans = 0
    for _, priority in print_list:
        priority_list[priority] += 1

    for priority in range(9,0,-1):
        priority_print_num = priority_list[priority]
        i = priority_print_num
        while i > 0:
            print_object = print_list.popleft()
            if print_object[1] == priority:
                ans += 1
                i -= 1
                if print_object[0] == m:
                    print(ans)
                    break
            else:
                print_list.append(print_object)
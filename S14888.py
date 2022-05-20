import sys
from collections import deque

sys.setrecursionlimit(100)
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
max_ans = -10 ** 9
min_ans = 10 ** 9

def calculate(number, operator):
    global max_ans, min_ans

    if len(number) == 1:
        if max_ans < number[0]:
            max_ans = number[0]
        if min_ans > number[0]:
            min_ans = number[0]
        return
    for op, op_count in enumerate(operator):
        if op_count != 0:
            num = deque(number)
            remain_operator = operator.copy()
            if op == 0:
                remain_operator[op] -= 1
                num.appendleft(num.popleft() + num.popleft())
                calculate(num, remain_operator)
            if op == 1:
                remain_operator[op] -= 1
                num.appendleft(num.popleft() - num.popleft())
                calculate(num, remain_operator)
            if op == 2:
                remain_operator[op] -= 1
                num.appendleft(num.popleft() * num.popleft())
                calculate(num, remain_operator)
            if op == 3:
                remain_operator[op] -= 1
                a = num.popleft()
                b = num.popleft()
                if (a < 0 and b > 0) or (a > 0 and b < 0):
                    num.appendleft((abs(a) // abs(b)) * (-1))
                else:
                    num.appendleft(a // b)
                calculate(num, remain_operator)

calculate(numbers, operators)
print(max_ans, min_ans)

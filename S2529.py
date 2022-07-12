from sys import stdin as st

k = int(st.readline())
inequality = list(st.readline().rstrip().split())

def max_inequal_num():
    ans = [0]
    idx = 0
    for i, sign in enumerate(inequality):
        if sign == '<':
            ans.append(i+1)
            idx = len(ans) - 1
        else:
            ans = ans[:idx] + [i+1] + ans[idx:]
    print(''.join(map(str, ans)))

def min_inequal_num():
    ans = [9]
    idx = 0
    for i, sign in enumerate(inequality):
        if sign == '>':
            ans.append(9-i-1)
            idx = len(ans) - 1
        else:
            ans = ans[:idx] + [9-i-1] + ans[idx:]
    print(''.join(map(str, ans)))

min_inequal_num()
max_inequal_num()

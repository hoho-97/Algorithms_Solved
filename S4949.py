from sys import stdin as st

line = st.readline().rstrip()

while line != '.':
    flag = True
    stack = []
    for s in line:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack:
                last = ''
            else:
                last = stack.pop()
            if last != '(' :
                flag = False
                print('no')
                break
        elif s == ']':
            if not stack:
                last = ''
            else:
                last = stack.pop()
            if last != '[':
                flag = False
                print('no')
                break
    if flag:
        if stack:
            print('no')
        else:
            print('yes')
    line = st.readline().rstrip()

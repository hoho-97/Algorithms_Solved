from sys import stdin as st
n = int(st.readline())
q = []
for _ in range(n):
    call = st.readline().split()
    if call[0] == 'push':
        q.append(call[1])
    call = call[0]
    if call == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif call == 'size':
        print(len(q))
    elif call == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif call == 'top':
        if q:
            print(q[-1])
        else:
            print(-1)
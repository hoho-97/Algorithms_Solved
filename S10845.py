from collections import deque
from sys import stdin as st
q = deque([])
for _ in range(int(st.readline())):
    call = st.readline().split()
    if call[0] == 'push':
        q.append(call[1])
        continue
    call = call[0]
    if call == 'pop':
        if not q:
            q.append(-1)
        print(q.popleft())
    elif call == 'size':
        print(len(q))
    elif call == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif call == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif call == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
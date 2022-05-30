from sys import stdin as st

t = int(st.readline())

for _ in range(t):
    q = set()
    k = int(st.readline())
    for __ in range(k):
        call = st.readline().rstrip().split()
        if call[0] == 'I':
            q.add(int(call[1]))
        if call[0] == 'D':
            if q:
                if call[1] == '-1':
                    q.remove(min(q))
                elif call[1] == '1':
                    q.remove(max(q))

    if not q:
        print('EMPTY')
    else:
        print(max(q), min(q))
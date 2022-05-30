from sys import stdin as st

m = int(st.readline())
ans = set()
for _ in range(m):
    call = st.readline().rstrip().split()
    if len(call) > 1:
        num = int(call[1])
    call = call[0]
    if call == 'add':
        if num not in ans:
            ans.add(num)
    elif call == 'remove':
        if num in ans:
            ans.remove(num)
    elif call == 'check':
        if num in ans:
            print(1)
        else:
            print(0)
    elif call == 'toggle':
        if num in ans:
            ans.remove(num)
        else:
            ans.add(num)
    elif call == 'all':
        ans = {i for i in range(1, 21)}
    elif call == 'empty':
        ans = set()
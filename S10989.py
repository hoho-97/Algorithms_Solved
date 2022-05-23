from sys import stdin as st

d = dict()
for i in range(int(st.readline())):
    m = int(st.readline())
    if m not in d.keys():
        d[m] = 1
    else:
        d[m] += 1

for k in sorted(d.keys()):
    for i in range(d[k]):
        print(k)
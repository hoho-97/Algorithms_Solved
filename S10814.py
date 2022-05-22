from sys import stdin as st

n = int(st.readline())
user = [[] for x in range(201)]
for _ in range(n):
    age, name = st.readline().split()
    user[int(age)].append(name)
for i in range(1,201):
    if user[i]:
        for name in user[i]:
            print("{0} {1}".format(i,name))
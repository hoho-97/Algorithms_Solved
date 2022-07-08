from sys import stdin as st

a1, b1 = map(int, st.readline().split())
a2, b2 = map(int, st.readline().split())
a = a1 * b2 + a2 * b1
b = b1 * b2

def GCB(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if a > b:
    c = GCB(a, b)
else:
    c = GCB(b, a)

print(a//c, b//c)

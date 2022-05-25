from sys import stdin as st

l = int(st.readline())
word = st.readline().rstrip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

ans = 0
for i, w in enumerate(word):
    ans += (alphabet.index(w)+1) * (31 ** i)

print(ans % 1234567891)
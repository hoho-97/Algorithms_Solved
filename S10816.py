from collections import Counter
from sys import stdin as st

n = int(st.readline())
sangguen = dict(Counter(list(map(int, st.readline().split()))))
m = int(st.readline())
questcard = list(map(int, st.readline().split()))

for card in questcard:
    if card in sangguen.keys():
        print(sangguen[card],end=" ")
    else:
        print(0,end=" ")
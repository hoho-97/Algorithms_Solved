import math
from sys import stdin as st
a, b, v = map(int, st.readline().split())
print(math.ceil((v-a)/(a-b))+1)
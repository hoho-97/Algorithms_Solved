from sys import stdin as st

n = int(st.readline())
scores = []
for _ in range(n):
    name, a, b, c = st.readline().split()
    a, b, c = map(int, (a, b, c))
    scores.append([name, a, b, c])
scores.sort(key=lambda x:x[0])
scores.sort(key=lambda x:x[3], reverse=True)
scores.sort(key=lambda x:x[2])
scores.sort(key=lambda x:x[1], reverse=True)

for score in scores:
    print(score[0])
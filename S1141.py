from sys import stdin as st

n = int(st.readline())
words = [st.readline().rstrip() for _ in range(n)]
words.sort(key=lambda x : len(x))
ans = 0

for i, word in enumerate(words):
    flag = True
    for j in range(i+1, n):
        if word == words[j][:len(word)]:
            flag = False
            break

    if flag:
        ans += 1

print(ans)
from sys import stdin as st

n = int(st.readline())
m = int(st.readline())
s = st.readline().rstrip()
count_ioi = 0
ans = 0
i = 0

while True:
    if i >= m-1:
        break

    if s[i:i+3] == 'IOI':
        count_ioi +=1
        i += 2

        if count_ioi >= n:
            ans += 1
            count_ioi -= 1
    else:
        i += 1
        count_ioi = 0

print(ans)
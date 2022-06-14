from sys import stdin as st

t = int(st.readline())

for _ in range(t):
    n = int(st.readline())
    scores = [tuple(map(int, st.readline().split())) for __ in range(n)]

    sorted_list = sorted(scores, key=lambda x: x[0], reverse=True)
    highest_rank = sorted_list.pop()[1]
    ans = 1

    while sorted_list:
        score = sorted_list.pop()

        if score[1] < highest_rank:
            highest_rank = score[1]
            ans += 1

    print(ans)
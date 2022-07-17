from sys import stdin as st

n = int(st.readline())
quiz = dict()
quiz_level = dict()
for i in range(1, 101):
    quiz[i] = set()

for _ in range(n):
    p, l = map(int, st.readline().split())
    quiz[l].add(p)
    quiz_level[p] = l

m = int(st.readline())
for _ in range(m):
    call = st.readline().split()
    l = 0
    if len(call) == 3:
        call, p, l = call
    else:
        call, p = call
    p, l = map(int, (p, l))

    if call == "recommend":
        if p == 1:
            for i in range(100, 0, -1):
                if quiz[i]:
                    print(max(quiz[i]))
                    break
        elif p == -1:
            for i in range(1, 101):
                if quiz[i]:
                    print(min(quiz[i]))
                    break
    elif call == "add":
        quiz[l].add(p)
        if p in quiz_level.keys():
            quiz[quiz_level[p]].remove(p)
        quiz_level[p] = l
    elif call == "solved":
        quiz[quiz_level[p]].remove(p)
        quiz_level.pop(p)
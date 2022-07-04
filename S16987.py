from sys import stdin as st

n = int(st.readline())
eggs = [list(map(int, st.readline().split())) for _ in range(n)]
ans = 0

def breakEgg(case, egg_index):
    global ans

    if egg_index == n:
        case_ans = 0
        for s, w in case:
            if s <= 0:
                case_ans += 1
        ans = max(ans, case_ans)
        return

    if case[egg_index][0] > 0:
        for i in range(n):
            no_unbreaken = True
            if i == egg_index:
                continue

            if case[i][0] > 0:
                no_unbreaken = False
                case[i][0] -= case[egg_index][1]
                case[egg_index][0] -= case[i][1]
                breakEgg(case, egg_index+1)
                case[i][0] += case[egg_index][1]
                case[egg_index][0] += case[i][1]

        if no_unbreaken:
            breakEgg(case, egg_index+1)
    else:
        breakEgg(case, egg_index+1)

breakEgg(eggs, 0)
print(ans)
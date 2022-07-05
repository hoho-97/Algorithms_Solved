from sys import stdin as st
from itertools import combinations

def observe(case):
    for tx, ty in teachers:
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]

            while True:
                if 0 > nx or n <= nx or 0 > ny or n <= ny:
                    break

                if case[nx][ny] == 'S':
                    return False
                elif case[nx][ny] == 'O':
                    break

                nx += dx[i]
                ny += dy[i]

    return True

n = int(st.readline())
hall = [list(st.readline().split()) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
non_block = []
teachers = []

for x in range(n):
    for y in range(n):
        if hall[x][y] == 'X':
            non_block.append((x, y))
        elif hall[x][y] == 'T':
            teachers.append((x, y))

for o1, o2, o3 in combinations(non_block, 3):
    case = []
    for line in hall:
        case.append(line[:])

    (x1, y1), (x2, y2), (x3, y3) = o1, o2, o3
    case[x1][y1], case[x2][y2], case[x3][y3] = 'O', 'O', 'O'

    simulation_res = observe(case)
    if simulation_res:
        print('YES')
        exit(0)
print('NO')
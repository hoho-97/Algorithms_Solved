from collections import deque
from sys import stdin as st


def print_ans(grid):
    for g in grid:
        print(''.join(g))

def bomb():
    next_grid = list(list(['O'] * c) for _ in range(r))

    for _x in range(r):
        for _y in range(c):
            if grid[_x][_y] == 'O':
                bomb_location.append((_x, _y))

    while bomb_location:
        x, y = bomb_location.popleft()

        if next_grid[x][y] == 'O':
            next_grid[x][y] = '.'

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < r and 0 <= ny < c:
                if next_grid[nx][ny] == 'O':
                    next_grid[nx][ny] = '.'

    return next_grid


r, c, n = map(int, st.readline().split())
grid = list(list(st.readline().rstrip()) for _ in range(r))
all_bomb_grid = list(list(['O'] * c) for _ in range(r))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
bomb_location = deque([])

if n == 1:
    print_ans(grid)
elif n % 2 == 0:
    print_ans(all_bomb_grid)
elif n % 4 == 3:
    grid = bomb()
    print_ans(grid)
elif n % 4 == 1:
    grid = bomb()
    grid = bomb()
    print_ans(grid)

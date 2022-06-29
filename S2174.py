from sys import stdin as st

a, b = map(int, st.readline().split())
n, m = map(int, st.readline().split())
field = [['' for _ in range(b)] for __ in range(a)]
robots = [(0, 0)]
direction = ['N', 'E', 'S', 'W']
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(1, n+1):
    x, y, d = st.readline().split()
    robots.append((int(x) - 1, int(y) - 1))
    field[int(x)-1][int(y)-1] = d

for _ in range(m):
    robot, call, roop = st.readline().split()
    robot, roop = int(robot), int(roop)
    x, y = robots[robot]
    robot_dir = field[x][y]

    if call == 'L':
        field[x][y] = direction[(direction.index(robot_dir) - roop) % 4]
    elif call == 'R':
        field[x][y] = direction[(direction.index(robot_dir) + roop) % 4]
    elif call == 'F':
        dir = direction.index(robot_dir)

        for i in range(roop):
            x, y = robots[robot]
            nx, ny = x + dx[dir], y + dy[dir]

            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                print('Robot {0} crashes into the wall'.format(robot))
                exit(0)
            else:
                if field[nx][ny] == '':
                    field[nx][ny] = field[x][y]
                    robots[robot] = (nx, ny)
                    field[x][y] = ''
                else:
                    crashed_robot = robots.index((nx, ny))
                    print('Robot {0} crashes into robot {1}'.format(robot, crashed_robot))
                    exit(0)

print('OK')
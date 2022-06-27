from collections import deque
from sys import stdin as st

n = int(st.readline())
k = int(st.readline())
board = [[0] * n for _ in range(n)]
board[0][0] = 1
sec = 0
for _ in range(k):
    x, y = map(int, st.readline().split())
    board[x - 1][y - 1] = 2
l = int(st.readline())
snake_move = deque([list(st.readline().rstrip().split()) for _ in range(l)])
snakeX, snakeY = 0, 0
snake_direction = 1  # 위, 오른쪽, 아래, 왼쪽 = 시계방향(0, 1, 2, 3)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
snake = deque([(0, 0)])

while True:
    sec += 1
    snakeX += dx[snake_direction % 4]
    snakeY += dy[snake_direction % 4]
    snake.append((snakeX, snakeY))

    if snakeX < 0 or snakeX >= n or snakeY < 0 or snakeY >= n:
        break
    if board[snakeX][snakeY] == 1:
        break

    if board[snakeX][snakeY] == 2:
        board[snakeX][snakeY] = 1
    elif board[snakeX][snakeY] == 0:
        board[snakeX][snakeY] = 1
        x, y = snake.popleft()
        board[x][y] = 0

    if snake_move:
        snake_turn = snake_move[0]

        if sec == int(snake_turn[0]):
            snake_move.popleft()

            if snake_turn[1] == 'L':
                snake_direction -= 1
            else:
                snake_direction += 1

print(sec)
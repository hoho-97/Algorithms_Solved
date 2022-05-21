from sys import stdin as st

n, m = map(int, input().split())
board = [list(st.readline().rstrip()) for i in range(n)]

def check_paint(x, y):
    global board
    count_start_W = 0
    count_start_B = 0
    for row in range(x, x + 8):
        for col in range(y, y + 8):
            color = board[row][col]
            if (row+col) % 2 == 0:
                if color == 'W':
                    count_start_B += 1
                else:
                    count_start_W += 1
            else:
                if color == 'W':
                    count_start_W += 1
                else:
                    count_start_B += 1
    return min(count_start_B, count_start_W)


ans = 64
result = ans
for i in range(n-7):
    for j in range(m-7):
        result = check_paint(i, j)
        if result < ans:
            ans = result
print(ans)
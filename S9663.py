n = int(input())
queen = [0 for _ in range(n)]
ans = 0

def dropQueen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        queen[x] = i
        check = checkQueen(x)
        if check:
            dropQueen(x+1)

def checkQueen(col_upStair):
    for col in range(col_upStair):
        if queen[col_upStair] == queen[col]:
            return False
        if abs(queen[col_upStair] - queen[col]) == col_upStair - col:
            return False
    return True

dropQueen(0)
print(ans)
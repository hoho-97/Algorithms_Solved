from sys import stdin as st

n, m = map(int, st.readline().split())
arr = [list(map(int, list(st.readline().rstrip()))) for _ in range(n)]
ans_arr = [list(map(int, list(st.readline().rstrip()))) for _ in range(n)]
ans = 0

def check():
    for x in range(n):
        for y in range(m):
            if arr[x][y] != ans_arr[x][y]:
                return False
    return True

def opposite(startX, startY):
    for x in range(startX, startX+3):
        for y in range(startY, startY+3):
            if arr[x][y] == 1:
                arr[x][y] = 0
            else:
                arr[x][y] = 1

for x in range(n-2):
    for y in range(m-2):
        if arr[x][y] != ans_arr[x][y]:
            opposite(x, y)
            ans += 1

if not check():
    print(-1)
else:
    print(ans)
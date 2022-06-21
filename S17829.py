from sys import stdin as st

n = int(st.readline())
arr = [list(map(int, st.readline().split())) for _ in range(n)]

dx, dy = [0, 0, 1, 1], [0, 1, 0, 1]

while True:
    if len(arr) == 1:
        break

    size = len(arr)
    next_arr = []

    for x in range(0, size, 2):
        row = []
        for y in range(0, size, 2):
            box = []

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                box.append(arr[nx][ny])
            box.sort()
            row.append(box[2])
        next_arr.append(row)

    arr = next_arr

print(arr[0][0])
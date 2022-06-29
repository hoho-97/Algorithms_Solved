from sys import stdin as st

n = int(st.readline())
higher_people_nums = list(map(int, st.readline().split()))
line = [11] * n

for height, higher_people in enumerate(higher_people_nums):
    height += 1
    i = 0
    while True:
        if higher_people == 0 and line[i] > height:
            line[i] = height
            break

        if line[i] > height:
            higher_people -= 1

        i += 1

print(*line)
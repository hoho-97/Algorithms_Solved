import sys
from sys import stdin as st

sys.setrecursionlimit(100)
n = int(st.readline())
paper = [list(map(int, st.readline().split())) for _ in range(n)]
ans = [0, 0, 0]

def check_paper(startX, startY, paper_size):
    global paper, ans
    first_paper_num = paper[startX][startY]

    if paper_size == 1:
        ans[first_paper_num+1] += 1
        return

    for x in range(startX, startX + paper_size):
        for y in range(startY, startY + paper_size):
            if paper[x][y] != first_paper_num:
                cutted_size = paper_size // 3
                for i in range(3):
                    for j in range(3):
                        check_paper(startX + cutted_size * i,
                                    startY + cutted_size * j,
                                    cutted_size)
                return

    ans[first_paper_num+1] += 1

check_paper(0, 0, n)
for i in range(3):
    print(ans[i])
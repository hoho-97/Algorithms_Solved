from sys import stdin as st

n, m = map(int, st.readline().split())
trees = list(map(int, st.readline().split()))

start = 1
end = max(trees)

def check_cutting(height):
    result = 0
    for tree in trees:
        cutted_tree = tree - height
        if cutted_tree > 0:
            result += cutted_tree
    if result >= m:
        return True
    else:
        return False

ans = 0
while start <= end:
    mid = (start + end) // 2

    if check_cutting(mid):
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)

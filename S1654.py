from sys import stdin as st
k, n = map(int, st.readline().split())

cables = [int(st.readline()) for _ in range(k)]
start = 1
end = max(cables)

def check_cutting(mid):
    cutting_cable = 0
    for cable in cables:
        cutting_cable += cable // mid

    if cutting_cable < n:
        return False
    else:
        return True

while start <= end:
    mid = (start + end) // 2
    if check_cutting(mid):
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)

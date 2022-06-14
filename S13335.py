from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
count = 0

while trucks:
    bridge.popleft()

    if sum(bridge) + trucks[0] <= l:
        truck = trucks.popleft()
        bridge.append(truck)
    else:
        bridge.append(0)
    count += 1

print(count + len(bridge))
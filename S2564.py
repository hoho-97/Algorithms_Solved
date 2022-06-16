from sys import stdin as st

def to_linear_point(direction, location):
    if direction == 1:
        return location
    elif direction == 2:
        return width + height + (width - location)
    elif direction == 3:
        return 2 * width + height + (height-location)
    elif direction == 4:
        return width + location

width, height = map(int, st.readline().split())
n = int(st.readline())
stores = [(map(int, st.readline().split())) for _ in range(n)]
donggeun_direction, donggeun_location = (map(int, st.readline().split()))
ans = 0

donggeun = to_linear_point(donggeun_direction, donggeun_location)

while stores:
    store_direction, store_location = stores.pop()
    store = to_linear_point(store_direction, store_location)

    route1 = abs(store - donggeun)
    full_route = 2 * (width + height)
    route2 = full_route - route1
    ans += min(route1, route2)

print(ans)
from sys import stdin as st

n, p = map(int, st.readline().split())
guitar = [[0] for _ in range(6)]
count = 0

for _ in range(n):
    guitar_string, guitar_flat = map(int, st.readline().split())

    if guitar[guitar_string-1]:
        if guitar[guitar_string-1][-1] < guitar_flat:
            guitar[guitar_string-1].append(guitar_flat)
            count += 1
        elif guitar[guitar_string-1][-1] > guitar_flat:
            while guitar[guitar_string-1]:
                if guitar[guitar_string-1][-1] <= guitar_flat:
                    break
                guitar[guitar_string-1].pop()
                count += 1

            if guitar_flat > guitar[guitar_string-1][-1]:
                guitar[guitar_string-1].append(guitar_flat)
                count += 1
    else:
        guitar[guitar_string-1].append(guitar_flat)
        count += 1
print(count)

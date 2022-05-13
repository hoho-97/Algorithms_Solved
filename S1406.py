import sys

cursor_front_word = list(sys.stdin.readline().rstrip())
cursor_back_word = list()
m = int(sys.stdin.readline())

for _ in range(m):
    req = sys.stdin.readline().rstrip()
    if req[0] == "P":
        req, x = req.split()

    if req == "L" and cursor_front_word:
        cursor_back_word.append(cursor_front_word.pop())
    elif req == "D" and cursor_back_word:
        cursor_front_word.append(cursor_back_word.pop())
    elif req == "B" and cursor_front_word:
        cursor_front_word.pop()
    elif req == "P":
        cursor_front_word.append(x)
cursor_front_word.extend(reversed(cursor_back_word))
print(''.join(cursor_front_word))
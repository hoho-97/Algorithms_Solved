n, m = map(int, input().split())
case = []

def permutation(count):
    global case

    if count == 0:
        print(*case)
        return

    for i in range(1, n+1):
        case.append(i)
        permutation(count-1)
        case.pop()

permutation(m)
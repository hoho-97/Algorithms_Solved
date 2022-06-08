from sys import stdin as st

while True:
    lotto = list(map(int, st.readline().split()))

    k = lotto[0]
    lotto = lotto[1:]
    if k == 0:
        break

    for num1 in range(k-5):
        for num2 in range(num1+1,k-4):
            for num3 in range(num2+1,k-3):
                for num4 in range(num3+1,k-2):
                    for num5 in range(num4+1,k-1):
                        for num6 in range(num5+1,k):
                            print(lotto[num1], lotto[num2], lotto[num3], lotto[num4],
                                  lotto[num5], lotto[num6],)
    print()
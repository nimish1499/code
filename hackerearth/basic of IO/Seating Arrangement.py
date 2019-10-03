for i in range(int(input())):
    n = int(input())
    s = n % 12
    if s == 0:
        n -= 11
    elif s < 7:
        n += (2 * (6 - s) + 1)
    else:
        n -= (2 * (s - 7) + 1)
    r = n % 6
    if r == 1 or r == 0:
        print(n, "WS")
    elif r == 2 or r == 5:
        print(n, "MS")
    else:
        print(n, "AS")

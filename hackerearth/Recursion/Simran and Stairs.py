def hop(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return hop(n - 1) + hop(n - 2) + hop(n - 3)


def main():
    n = int(input())
    y = hop(n)
    print(y)


main()

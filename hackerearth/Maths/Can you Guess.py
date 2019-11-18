for i in range(int(input())):
    n = int(input())
    a = []
    s = 0
    for j in range(1, n+1):
        if n % j == 0:
            a.append(j)
    for j in a:
        s += j
    print(s-n)

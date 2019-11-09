t = int(input())
for i in range(t):
    c = 0
    n = int(input())
    a = list(map(int, input().split()))
    l = len(a)
    for j in range(l):
        for k in range(j+1, l):
            if a[j] == a[k]:
                pass
            elif (a[j] + a[k]) % 2 == 0:
                c = c + 1
    print(c)

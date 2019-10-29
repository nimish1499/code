t = int(input())
c = 0
for i in range(t):
    m = int(input())
    a = []
    k = 0
    for j in range(100000):
        c = j//5 + j//25 + j//125 + j//625 + j//3125 + j//15625 + j//78125
        if c == m:
            a.append(j)
            k = k + 1
    print(k)
    if k == 5:
        print(" ".join(map(str, a)))


m = int(input())
a = []
b = []
for i in range(m):
    x = int(input())
    a.append(x)
a.sort()
for i in range(1, m):
    y = a[i] - a[i-1]
    b.append(y)
minimum = min(b)
for i in range(2, minimum+1):
    if minimum % i == 0:
        print(i, end = " ")

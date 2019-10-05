d = int(input())
c = 0
for i in range(d):
    r, x = map(int, input().split())
    td = 100 * x
    tr = (2 * 22 * r)//7
    if td >= tr:
        c += 1
print(c)

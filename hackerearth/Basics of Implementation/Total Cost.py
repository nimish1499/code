p, s, t, h, x = map(int, input().split())
s1 = 0
while x > 0:
    if s > t:
        s1 += p
    elif s <= t:
        s1 += h
    s = s-1
    x = x-1
print(s1)


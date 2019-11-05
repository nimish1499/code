def solve(x):
    if x<9:
        return x
    else:
        return x%9 +10*solve(x//9)


from    sys import stdin as inp
N = inp.read().split()
for i in N:
    print(solve(int(i)))

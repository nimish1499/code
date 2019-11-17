from functools import reduce

n = int(input())
a = list(map(int, input().split()))
p = 1

def GCD(a, b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def GCD_List(a):
    return reduce(GCD, a)


for i in a:
    p = p*i
print(p**GCD_List(a)%((10**9)+7))

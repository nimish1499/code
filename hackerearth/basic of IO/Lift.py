t = int(input())
a = 0
b = 7
for i in range(0, t):

    n = int(input())

    if n - a > b - n:
        print("B")
        b = n
    elif n - a < b - n:
        print("A")
        a = n
    elif n - a == b - n:
        print("A")
        a = n

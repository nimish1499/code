m = int(input())
a = list(map(int, input().split()))
b = len(a)
c = []
d = 0
for i in range(b):
    x = a[b-1] % 100
    d = x % 10
    if d % 10 == 0:
        print("Yes")
        break
    else:
        print("No")
        break

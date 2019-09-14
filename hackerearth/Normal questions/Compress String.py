Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = input()
a = list(s)
n = len(a)
c = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        c += 1
    elif c >= 1:
        print(a[i]+str(c+1),end="")
        c = 0
    elif c == 0:
        print(a[i], end="")
if a[n-1] != a[n-2]:
    print(a[n-1],end="")


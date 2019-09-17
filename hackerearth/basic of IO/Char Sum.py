Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input()
s = 0
d = 0
for i in a:
    l = len(i)
    while l != 0:
        s = s + (ord(i) - 96)
        l = l - 1
print(s)

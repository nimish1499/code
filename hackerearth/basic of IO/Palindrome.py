Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = (input())
str = ""
for i in name:
    str = i + str



if str == name:
    print("YES")
else:
    print("NO")

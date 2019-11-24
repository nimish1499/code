Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input()
toggle = ""
if 1 <= len(name) <= 100:
    for i in name:
        if i.isupper():
            toggle += i.lower()
        if i.islower():
            toggle = toggle + i.upper()
print(toggle)


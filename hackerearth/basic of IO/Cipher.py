name = input()
k = int(input())
for i in name:
    b = ord(i)
    if 48 <= b <= 57:
        a = ((ord(i) - 48 + k)%10)+48
        print(chr(a), end="")
    elif 65 <= b <= 90:
        c = ((ord(i) - 65 + k)%26)+65
        print(chr(c), end="")
    elif 97 <= b <= 122:
        d = ((ord(i) + k-97)%26)+97
        if d>122:
            d = 97 + (d-122)
        if d >= 123:
            print(chr(d), end="")
    else:
        e = chr(b)
        print(e, end="")

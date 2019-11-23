a = input()
if (ord(a[0]) + ord(a[1])) % 2 == 0 and (ord(a[3]) + ord(a[4])) % 2 == 0 and (ord(a[5]) + ord(a[4])) % 2 == 0 and (
        ord(a[7]) + ord(a[8])) % 2 == 0 and a[2] not in ("A", "E", "I", "O", "U", "Y"):
    print("valid")
else:
    print("invalid")

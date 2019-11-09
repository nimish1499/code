t = int(input())
for i in range(t):
    s = input()
    sum = 0
    su = ""
    a = []
    str = ""
    str1 = ""
    for j in s:
        str = j + str
    for j in range(len(s)):
        sum = (((ord(str[j])-97)%26) + ((ord(s[j])-96)%26))% 26
        su = chr(sum+97)
        a.append(su)
    for j in a:
        print(j, end="")
    print()

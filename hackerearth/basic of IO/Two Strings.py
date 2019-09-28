t = int(input())
for i in range(t):
    s, s1 = input().split()
    a = [0]*26
    b = [0]*26
    for j in s:
        a[ord(j)-97] += 1
    for k in s1:
        b[ord(k)-97] += 1
    if a == b:
        print("YES")
    else:
        print("NO")

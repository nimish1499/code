t = int(input())
for i in range(t):
    b = [0] * 26
    c = [0] * 26
    sum1 = 0
    s = input()
    s1 = input()
    for j in s:
        b[ord(j)-97] += 1
    for k in s1:
        c[ord(k)-97] += 1
    for j in range(26):
        if c[j] != b[j]:
            sum1 += abs(b[j] - c[j])
    print(sum1)


n = int(input())
a = list(input().split())
p = 1
for i in a:
    p = (p * int(i)) % ((10**9)+7)
print(p)


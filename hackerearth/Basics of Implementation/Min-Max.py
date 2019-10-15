n = int(input())
a = list(map(int, input().split()))
l = len(a)
max_val = max(a)
min_val = min(a)
c = 0
for i in range(min_val+1, max_val, 1):
    if i in a:
        c = c+1
    else:
        pass
if c == max_val-min_val-1:
    print("YES")
else:
    print("NO")

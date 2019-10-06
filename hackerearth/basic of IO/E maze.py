s1 = input()
s = s1.upper()
x = 0
y = 0
for i in s:
    if i == 'R':
        x = x+1
    if i == 'L':
        x = x-1
    if i == 'U':
        y = y+1
    if i == 'D':
        y = y-1
print(x, y)

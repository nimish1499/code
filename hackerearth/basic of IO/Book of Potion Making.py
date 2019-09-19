n = input()
k = 1
s = 0
for i in n:
    s = (int(i) * k) +s
    k = k + 1
if s % 11 == 0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")

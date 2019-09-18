c = 0    
for i in range(0, 13):
   try:
    m, n = input().split()
    mo = int(m)
    no = int(n)
    if (0 <= no) & (mo <= (10 ** 98)):
        c = mo + no
        print(c)
   except: 
    break

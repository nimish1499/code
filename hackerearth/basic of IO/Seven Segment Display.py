t = int(input())
for i in range(t):
    n = input()
    s = 0
    for j in n:
        b = 0
        if j == '0':
            b = 6
        if j == '1':
            b = 2
        if j == '2':
            b = 5
        if j == '3':
            b = 5
        if j == '4':
            b = 4
        if j == '5':
            b = 5
        if j == '6':
            b = 6
        if j == '7':
            b = 3
        if j == '8':
            b = 7
        if j == '9':
            b = 6
        s += b
    if s % 2 == 0:
        for k in range(s//2):
            print('1', end="")
        print()    
    if s % 2 != 0:
        print('7', end="")
        for k in range((s//2)-1):
            print('1', end="")
        print()
        

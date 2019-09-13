N = int(input())
for i in range(N):
    sh, sm, eh, em = map(int, input().split())
    a = eh - sh 
    b = em - sm
    if b >= 0:
        c = b
        d = a
    elif b < 0:
        c = b+60
        d = a-1
    print(d, c)


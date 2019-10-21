t = int(input())
n = 0
m = 0
if 1 <= t <= 20:
    for i in range(1, t + 1):
        n, m = input().split()
        no = int(n)
        mo = int(m)

        if (1 <= no <= 100) & (1 <= mo <= (10 ** 5)):
            if mo % no == 0:
                print("Yes")
            else:
                print("No")

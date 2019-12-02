for _ in range(int(input())):
    n = int(input())
    m = (10**9)+7
    s = (n%m *(2*n%m - 1))%m
    print(s)

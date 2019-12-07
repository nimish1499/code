while True:
    try:
        n = int(input())
        a = bin(n)
        print(a.count('1'))
    except:
        break

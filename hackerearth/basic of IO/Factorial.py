
num = int(input())
fact = 1
if 1 <= num <= 10:
    for i in range(1, num + 1):
        fact = fact * i
    print (fact)

def prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        pun = str(number)
        print(pun +" ", end="")


def lim(limit):
    for j in range(1, limit):
        prime(j)


def main():
    limit = int(input())
    lim(limit)


main()


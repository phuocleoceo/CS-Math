from math import ceil, sqrt


def Eratosthenes(n):
    isPrime = [0]*(n+1)
    for i in range(2, n+1):
        isPrime[i] = 1

    for i in range(2, ceil(sqrt(n))+1):
        if isPrime[i] == 1:
            for j in range(i*2, n+1, i):
                isPrime[j] = 0

    quant = 0
    for i in range(2, n+1):
        if isPrime[i] == 1:
            print(i, end=" ")
            quant = quant+1

    print("\n>> Quantity : ", quant)


Eratosthenes(2000)

import math


# Phân tích n thành tích các số nguyên tố
def PhanTich(n):
    result = {}
    for i in range(2, n+1):
        dem = 0
        while n % i == 0:
            dem += 1
            n = n//i
        if dem != 0:
            result[i] = dem
    return result


# Số ước số
def SoUocSo(n):
    result = 1
    for value in PhanTich(n).values():
        result *= value+1
    return result


def TongUocSo(n):
    result = 1
    for key, value in PhanTich(n).items():
        result *= (math.pow(key, value+1)-1)/(key-1)
    return result


def TichUocSo(n):
    return math.pow(n, SoUocSo(n)/2)


def Tich(n):
    result = 1
    for i in range(1, n+1):
        if n % i == 0:
            result *= i
    return result


N = 10000
print(PhanTich(N))
print(SoUocSo(N))
print(TongUocSo(N))
print(TichUocSo(N))
print(Tich(N))

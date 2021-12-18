import math


# Nghịch đảo module m của a là a^-1 sao cho  a.a^-1 mod(m) = 1
# Tức là tìm 1 số i để (a*i-1) chia hết cho m
# a^-1 chỉ tồn tại khi gcd(a,m)=1 - nguyên tố cùng nhau
def ModularInverse(a, m):
    if math.gcd(a, m) != 1:
        return None

    i = 0
    while True:
        if (a*i-1) % m == 0:
            return i
        else:
            i = i+1


def ChineseTheorem(a, m):
    n = len(a)
    M = 1
    for x in m:
        M = M*x

    Mi = [0]*n
    y = [0]*n
    x = 0
    for i in range(0, n):
        Mi[i] = int(M/m[i])
        y[i] = ModularInverse(Mi[i], m[i])
        x = x+a[i]*Mi[i]*y[i]

    return Optimize(x, M)


def Optimize(x, M):
    # Tìm i nhỏ nhất để i*M>x
    i = 0
    while i*M < x:
        i = i+1
    # Trừ x đi một lượng (i-1)*M để nó vẫn > 0
    return x-(i-1)*M, M


# print(ModularInverse(8, 6))

a = [2, 3, 5]
m = [3, 5, 7]
x, M = ChineseTheorem(a, m)
print(str(x)+"(mod"+str(M)+")")

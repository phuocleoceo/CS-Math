from math import gcd


def ModularInverse(a, m):
    if gcd(a, m) == 1:
        i = 0
        while True:
            if (a*i-1) % m == 0:
                return i
            else:
                i = i+1
    else:
        return None


def ChineseTheorem(a, m):
    n = len(a)
    M = 1
    for x in m:
        M = M*x
    mi = [0]*n
    y = [0]*n
    x = 0
    for i in range(0, n):
        mi[i] = M//m[i]
        y[i] = ModularInverse(mi[i], m[i])
        x = x+a[i]*mi[i]*y[i]
    return Optimize(x, M)


def Optimize(x, M):
    # Tìm i nhỏ nhất để i*M>x
    i = 0
    while i*M < x:
        i = i+1
    # Trừ x đi một lượng (i-1)*M để nó vẫn > 0
    return x-(i-1)*M, M


a = [2, 3, 4]
m = [3, 5, 11]
x, M = ChineseTheorem(a, m)
print(str(x)+"(mod"+str(M)+")")

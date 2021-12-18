import numpy as np


# Ma trận chuyển vị
def Transpose_Matrix(A):
    AT = np.zeros_like(A)
    m, n = A.shape
    for i in range(0, m):
        for j in range(0, n):
            AT[i][j] = A[j][i]
    return AT


# Copy ma trận
def Copy_Matrix(M):
    rows, cols = len(M), len(M[0])
    N = np.zeros((rows, cols))
    for i in range(0, rows):
        for j in range(0, cols):
            N[i][j] = M[i][j]
    return N


# Định thức
def Determinant_Matrix(M):
    n = len(M)
    A = Copy_Matrix(M)
    count = 0
    B = [0]*n

    for i in range(0, n-1):
        if A[i][i] == 0:
            check = 0

            for j in range(i+1, n):
                if A[i][j] != 0:
                    for k in range(0, n):
                        A[k][i], A[k][j] = A[k][j], A[k][i]
                    count += 1
                    check += 1
                    break
            if check == 0:
                return 0

        B[i] = A[i][i]
        for j in range(0, n):
            A[i][j] /= B[i]

        for j in range(i+1, n):
            scale = A[j][i]
            for k in range(0, n):
                A[j][k] -= scale*A[i][k]

    B[n-1] = A[n-1][n-1]
    det = 1.0
    for i in range(0, n):
        det *= B[i]

    if count % 2 == 0:
        return det
    else:
        return -det


# Ma trận bù, bỏ hàng i cột j
def Minor_Matrix(A, i, j):
    A = A.tolist()
    return [row[:j] + row[j+1:] for row in (A[:i]+A[i+1:])]


# Ma trận nghịch đảo
def Inverse_Matrix(A):
    det = Determinant_Matrix(A)
    n = len(A)

    if det == 0:
        return None

    if n == 1 and len(A[0]) == 1:
        return 1/A[0][0]

    A_Inv = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0, n):
            P = Minor_Matrix(A, i, j)
            A_Inv[i][j] = 1/det*pow(-1, i+j)*Determinant_Matrix(P)
    return Transpose_Matrix(A_Inv)


A = np.array([[1, 2, 3],
              [4, 3, 6],
              [6, 8, 9]])
print(Transpose_Matrix(A))

print(Determinant_Matrix(A))

print(Inverse_Matrix(A))

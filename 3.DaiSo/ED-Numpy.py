from numpy import roots, diag
from numpy.linalg import inv
from math import pow
import numpy as np


# Copy ma trận
def Copy_Matrix(M):
    return np.array([x for x in M])


# Ma trận Phorebemit theo phương pháp Danhilepski
def Phorebemit_Matrix(a):
    n = len(a)
    A = Copy_Matrix(a)
    M, M1, B = np.zeros((n, n)), np.zeros((n, n)), np.zeros((n, n))
    M_Eigenvector = np.identity(n)

    for k in range(n-1, 0, -1):
        for i in range(0, n):
            for j in range(0, n):
                if i != k-1:
                    if i == j:
                        M[i][j] = 1
                        M1[i][j] = 1
                    else:
                        M[i][j] = 0
                        M1[i][j] = 0
                else:
                    M1[i][j] = A[k][j]
                    if j == k-1:
                        M[i][j] = 1/A[k][k-1]
                    else:
                        M[i][j] = -A[k][j]/A[k][k-1]
        B = A.dot(M)
        A = M1.dot(B)
        M_Eigenvector = M_Eigenvector.dot(M)

    return A, M_Eigenvector


# Vector chứa Giá trị riêng Ma trận
def Eigenvalue_Matrix(A):
    Phorebemit_Mat, _ = Phorebemit_Matrix(A)
    return [1.0]+[-x for x in Phorebemit_Mat[0]]


# Ma trận vecto riêng
def Eigenvector(M, Eigenvalue):
    n = len(Eigenvalue)
    A, RESULT_VECTOR = np.zeros((n, n)), np.zeros((n, n))

    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = pow(Eigenvalue[i], n-j-1)
        RESULT_VECTOR[i] = M.dot(A[i])

    return RESULT_VECTOR.T


# A = [[2, 1, 0],
#      [1, 3, 1],
#      [0, 1, 2]]
A = np.array([[2, 1],
              [4, 5]])

Eigenvalue = roots(Eigenvalue_Matrix(A))

Eigenvector_Matrix = Eigenvector(Phorebemit_Matrix(A)[1], Eigenvalue)

print("A phân rã thành : ")

V = Eigenvector_Matrix
print("Ma trận vector riêng (V) : ")
print(V)

print("Ma trận giá trị riêng (diag(lamda)) : ")
diag_eigen = diag(Eigenvalue)
print(diag_eigen)

print("Ma trận vector riêng nghịch đảo (V^(-1)) : ")
V_inv = inv(Eigenvector_Matrix)
print(V_inv)

# print("Kiểm tra kết quả : ", V.dot(diag_eigen).dot(V_inv))

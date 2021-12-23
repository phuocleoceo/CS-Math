import numpy as np
from numpy.linalg import eigvals


def cholesky_decomposition(A):
    L = np.zeros_like(A)
    n = len(A)
    for j in range(n):
        for i in range(j, n):
            if i == j:
                sumk = 0
                for k in range(j):
                    sumk += L[i, j]**2
                L[i, j] = np.sqrt(A[i, j]-sumk)
            else:
                sumk = 0
                for k in range(j):
                    sumk += L[i, k]*L[j, k]
                L[i, j] = (A[i, j]-sumk)/L[j, j]
    return L


# Ma trận đối xứng
def is_symmetric_matrix(A):
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if A[i, j] != A[j, i]:
                return False
    return True


# Ma trận xác định dương, nghĩa là mọi giá trị riêng phải dương
def is_positive_definite_matrix(V):
    for x in V:
        if x <= 0:
            return False
    return True


# Kiểm tra điều kiện để phân rã
def matrix_can_use_cholesky(A):
    m, n = A.shape
    if m != n:
        print(">> Ma tran A khong vuong !")
        return False

    if not is_symmetric_matrix(A):
        print(">> Ma tran A khong doi xung !")
        return False

    V = eigvals(A)
    if not is_positive_definite_matrix(V):
        print(">> Ma tran A khong xac dinh duong !")
        return False
    return True


A = np.array([[5, -2],
              [-2, 7]], dtype=float)
if matrix_can_use_cholesky(A):
    L = cholesky_decomposition(A)
    print("> L : \n", L)
    print("> Kiem tra L.LT : \n", L.dot(L.T))
else:
    print("Matrix A cannot use cholesky decomposition")

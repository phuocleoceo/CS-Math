import math
import numpy as np


def SortEigenValAndVector(S, V):
    temp = list(zip(S, V))
    S.sort(reverse=True)
    temp.sort(key=lambda x: x[0], reverse=True)
    return np.array([i[1] for i in temp]).T


def SVD(A):
    m, n = np.shape(A)
    U = np.zeros((m, m), dtype=float)
    D = np.zeros((m, n), dtype=float)
    V = np.zeros((n, n), dtype=float)
    S, V = np.linalg.eig(np.dot(A.T, A))

    V = SortEigenValAndVector(list(S), V.T)

    if m > n:
        for i in range(0, n):
            D[i][i] = math.sqrt(S[i])
        for i in range(0, n):
            U[i] = np.dot(A, V.T[i]) / D[i][i]
    else:
        for i in range(0, m):
            D[i][i] = math.sqrt(S[i])
        for i in range(0, m):
            U[i] = np.dot(A, V.T[i]) / D[i][i]
    return U.T, D, V


A = np.array([[1, 3.8, 5],
              [7, 8, 9.5]])

U, D, V = SVD(A)

print(">> Matrix U: \n", U)

print(">> Matrix D: \n", D)

print(">> Matrix V: \n", V)

print("U.D.VT : \n", (U.dot(D)).dot(V.T))
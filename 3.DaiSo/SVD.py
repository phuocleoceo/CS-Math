from numpy.linalg import eig
from math import sqrt
import numpy as np


def SVD(A):
    m, n = np.shape(A)
    U = np.zeros((m, m))
    D = np.zeros((m, n))
    V = np.zeros((n, n))

    ATA = A.T.dot(A)
    S, V = eig(ATA)

    t = list(zip(S, V))
    t.sort(key=lambda x: x[0], reverse=True)
    S = np.array([i[0] for i in t])
    V = np.array([i[1] for i in t])

    loop = min(m, n)
    for i in range(loop):
        D[i][i] = sqrt(S[i])
        U[i] = A.dot(V.T[i]) / D[i][i]
    return U.T, D, V


A = np.array([[-1, 3, 5],
              [7, 8.6, 9]])

U, D, V = SVD(A)

print(">> Matrix U: \n", U)

print(">> Matrix D: \n", D)

print(">> Matrix V: \n", V)

print("U.D.VT : \n", (U.dot(D)).dot(V.T))

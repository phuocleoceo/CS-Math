import numpy as np


def RightTurn(p, q, r):
    d1 = (r[1]-p[1])*(q[0]-p[0])
    d2 = (q[1]-p[1])*(r[0]-p[0])
    return d1 < d2


def ConvexHull(P):
    sorted(P, key=lambda x: x[0])
    L_upper = [P[0], P[1]]
    for i in range(2, len(P)):
        L_upper.append(P[i])
        while len(L_upper) > 2 and not RightTurn(L_upper[-1], L_upper[-2], L_upper[-3]):
            del L_upper[-2]
    L_lower = [P[-1], P[-2]]
    for i in range(len(P)-3, -1, -1):
        L_lower.append(P[i])
        while len(L_lower) > 2 and not RightTurn(L_lower[-1], L_lower[-2], L_lower[-3]):
            del L_lower[-2]
    del L_lower[0]
    del L_lower[-1]
    L = L_upper + L_lower
    return np.array(L[::-1])


if __name__ == '__main__':
    P = np.array([(3, 4),
                  (5, 3),
                  (6, 5),
                  (7, 6),
                  (8, 7),
                  (4, 9),
                  (3, 8),
                  (4, 8),
                  (7, 10),
                  (7, 4)])
    print(ConvexHull(P))

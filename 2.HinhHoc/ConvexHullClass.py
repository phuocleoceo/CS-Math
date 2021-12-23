import numpy as np


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def RightTurn(p, q, r):
    return (q.x*r.y+p.x*q.y+p.y*r.x)-(q.x*p.y+q.y*r.x+p.x*r.y) < 0


def ConvexHull(P):
    sorted(P, key=lambda p: p.x)
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
    return np.array(L[:-1])


if __name__ == '__main__':
    P = np.array([Point(3, 4),
                  Point(5, 3),
                  Point(6, 5),
                  Point(7, 6),
                  Point(8, 7),
                  Point(4, 9),
                  Point(3, 8),
                  Point(4, 8),
                  Point(7, 10),
                  Point(7, 4)])
    for ch in ConvexHull(P):
        print("(", ch.x, ",", ch.y, ")")

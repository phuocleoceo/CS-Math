import numpy as np


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def NotRightTurn(p, q, r):
    return (q.x*r.y+p.x*q.y+p.y*r.x)-(q.x*p.y+q.y*r.x+p.x*r.y) >= 0


def ConvexHull(P):
    sorted(P, key=lambda p: p.x)
    L = len(P)

    Lupper = [P[0], P[1]]
    for i in range(2, L):
        Lupper.append(P[i])
        while len(Lupper) > 2 and NotRightTurn(Lupper[-1], Lupper[-2], Lupper[-3]):
            del Lupper[-2]

    Llower = [P[-1], P[-2]]
    for i in range(L-3, -1, -1):
        Llower.append(P[i])
        while len(Llower) > 2 and NotRightTurn(Llower[-1], Llower[-2], Llower[-3]):
            del Llower[-2]

    L = Lupper + Llower[1:-1]
    return L[:-1]


P = [Point(3, 4),
     Point(5, 3),
     Point(6, 5),
     Point(7, 6),
     Point(8, 7),
     Point(4, 9),
     Point(3, 8),
     Point(4, 8),
     Point(7, 10),
     Point(7, 4)]
for p in ConvexHull(P):
    print("(", p.x, ",", p.y, ")")

from math import exp
import numpy as np
import matplotlib.pyplot as plt


def grad(x):  # f'(x)
    return 2*exp(2*x)+6*exp(x)*x-14*exp(x)+20*x-60


def cost(x):  # f(x)
    return (exp(x)+3*x-10)**2+x**2


# def GD_momentum(x_init, gamma=0.1, alpha=0.9, N=1000, esilon=1e-5):
#     theta = [x_init]
#     v_old = np.zeros_like(x_init)
#     for it in range(N):
#         v_new = alpha*v_old + gamma*grad(theta[-1])
#         theta_new = theta[-1] - v_new
#         if np.abs(grad(theta_new)) < esilon:
#             break
#         theta.append(theta_new)
#         v_old = v_new
#     return theta, it


# if __name__ == '__main__':
#     x, it = GD_momentum(1.5, gamma=0.1, alpha=0.9)

#     print("Momentum_Solution : ")
#     print("x = ", x[-1])
#     print("cost = ", cost(x[-1]))
#     print("After", it, "iterations")

x = range(0, 100)
y = [cost(i) for i in x]
plt.plot(x, y)
plt.show()

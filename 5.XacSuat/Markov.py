import numpy as np
from numpy.linalg import matrix_power

# Vecto xác suất trạng thái
X = np.array([0.7, 0.3])
X = X.T

# Ma trận xác suất chuyển vị
P = np.array([[0.6, 0.4],
              [0.4, 0.6]])

# Xn = P^n * X

# Sau n giai đoạn
n = 2
print(matrix_power(P, n).dot(X))

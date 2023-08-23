import numpy as np


A = np.mat("0 1 2;1 0 3;4 -3 8")

print("A\n", A)

# 使用inv函数计算逆矩阵

inverse = np.linalg.inv(A)
print("inverse of A\n", inverse)

print("check\n", A * inverse)

A = np.mat("1 -2 1;0 2 -8;-4 5 9")
print("A\n", A)
b = np.array([0, 8, -9])
print("b\n", b)
x = np.linalg.solve(A, b)
print("Solution", x)
print("Check\n", np.dot(A, x))

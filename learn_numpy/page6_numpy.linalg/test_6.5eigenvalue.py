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

# 求解特征值和特征向量
A = np.mat("3 -2;1 0")
print("A\n", A)
print("eigenvalue", np.linalg.eigvals(A))
# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eig", eigenvalues)
print("Second tuple of eig\n", eigenvectors)

# 使用dot函数验证求得的解是否正确。分别计算等式 Ax = ax 的左半部分和右半部分，
# 检查是否相等。
for i in range(len(eigenvalues)):
    print("Left", np.dot(A, eigenvectors[:,i]))
    print("Right", eigenvalues[i] * eigenvectors[:,i])


# SVD（Singular Value Decomposition，奇异值分解）是一种因子分解运算，
# 将一个矩阵分解为3个矩阵的乘积。奇异值分解是前面讨论过的特征值分解的一种推广。
# 在numpy.linalg模块中的svd函数可以对矩阵进行奇异值分解。
# 该函数返回3个矩阵——U、Sigma和V，其中U和V是正交矩阵，Sigma包含输入矩阵的奇异值。


A = np.mat("4 11 14;8 7 -2")
print("A\n", A)
U, Sigma, V = np.linalg.svd(A, full_matrices=False)
print("U\n", U)
print("sigma", Sigma)
print("V", V)

# 使用diag函数生成完整的奇异值矩阵
print("product\n", U* np.diag(Sigma) * V )


A = np.mat("4 11 14;8 7 -2")
print("A\n", A)

pseudoinv = np.linalg.pinv(A)
print("Pseudo inverse\n", pseudoinv)

print("Check", A * pseudoinv)
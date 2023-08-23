# 矩阵 matrix
import numpy as np

A = np.mat('1 2 2;1 2 3 ;6 8 8')
print(A)

print("A.T", A.T)

print("A.I\n", A.I)

print("Creation from array", np.mat(np.arange(9).reshape(3, 3)))

print("Check Inverse", A * A.I)

# 利用一些已有的较小的矩阵来创建一个新的大矩阵
# 这可以用bmat函数来实现。这里的b表示“分块”，bmat即分块矩阵（block matrix）

A = np.eye(2)
print("A\n", A)

B = 2 * A
print("B\n", B)

print("compound matrix\n", np.bmat("A B;A B"))
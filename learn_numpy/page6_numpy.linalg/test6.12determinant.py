import numpy as np

# 行列式 计算了矩阵的行列式
import numpy as np
A = np.mat("3 4;5 6")
print("A\n", A)
print("Determinant", round(np.linalg.det(A)))
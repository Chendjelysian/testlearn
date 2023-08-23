# fill函数可以将数组元素的值全部设置为一个指定的标量值，
# 它的执行速度比使用array.flat = scalar或者用循环遍历数组赋值的方法更快。
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

x = np.arange(5)
print("EXP", np.exp(x))

# linspace ,起始，终止，元素分段数量
print("Linspace", np.linspace(-1, 0, 5))

N = int(5)
weights = np.exp(np.linspace(-1. , 0. , N))

# 对权重值做归一化处理。我们将用到ndarray对象的sum方法。
weights /= weights.sum()
print("Weights", weights )

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

# 布林线略

# 线姓模型预测价格
b = c[-N:]
b = b[::-1]
print(b)

A = np.zeros((N, N), float)
print(A)

for i in range(N):
    A[i, ] = c[-N - 1 - i: - 1 - i]
print(A)
# linalg包是专门用于线性代数计算的
(x, residuals, rank, s) = np.linalg.lstsq(A, b)
print(x, residuals, rank, s)
# 返回的元组中包含稍后要用到的系数向量x、一个残差数组、A的秩以及A的奇异值
# 一旦得到了线性模型中的系数，我们就可以预测下一次的股价了。使用NumPy中的dot
# 函数计算系数向量与最近N个价格构成的向量的点积（dot product）

print(np.dot(b, x))

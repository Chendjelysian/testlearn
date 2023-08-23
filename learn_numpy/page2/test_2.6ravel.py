import numpy
import numpy as np


b = np.arange(24).reshape(2, 3, 4)
print(b.shape)
print(b)
print("\n")
# ravel只返回结果视图
print(b.ravel())
# flatten分配内存
print(b.flatten())

b.shape = (6, 4)
print(b)
# 转置
print(b.transpose())



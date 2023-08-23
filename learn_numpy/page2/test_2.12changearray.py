import numpy
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)

b = 2 * a
print(b)

# 转换成列表
c = np.array([1.j + 1, 2.j + 3])
print(c)

print(c.tolist())
# astype函数
print(c.astype(int))
# 保留虚部
print(c.astype('complex'))



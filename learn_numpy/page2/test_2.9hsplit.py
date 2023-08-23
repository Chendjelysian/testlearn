import numpy
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)

b = 2 * a
print(b)
# 水平分割
print(np.hsplit(a, 3) )
print(np.split(a, 3, axis=1))
# 垂直分割
print(np.vsplit(a,3))

print(np.vsplit(a, 3) )
print(np.split(a, 3, axis=0) )

c = np.arange(27).reshape(3, 3, 3)
print(c)
print(np.dsplit(c, 3) )
import numpy
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)

b = 2 * a
print(b)
# ndim 给出数组的维数或者数组轴的个数
print(b.ndim)
# 数组元素总个数
print(b.size)
# 字节数
print(b.itemsize)
# 数组空间
print(b.nbytes)
# 转置
print(b.T)
# 复数数组
c = np.array([1.j + 1, 2.j + 3])
print(c)

# real 给出复数数组的实部
print(c.real)

# imag 给出虚部
print(c.imag)

# 数组有复数，数据类型就会自动变回复数型
print(c.dtype)
print(c.dtype.str)

# flat 获得一个扁平的一维数组
b = np.arange(4).reshape(2,2)
print(b)

f = b.flat
print(f)

for item in f:
    print(item)

# 我们还可以用flatiter对象直接获取一个数组元素：
# In: b.flat[2]
# Out: 2
# 或者获取多个元素：
# In: b.flat[[1,3]]
# Out: array([1, 3])
# flat属性是一个可赋值的属性。对flat属性赋值将导致整个数组的元素都被覆盖：
# In: b.flat = 7
# In: b
# Out:
# array([[7, 7],
#  [7, 7]])
# or selected elements
# In: b.flat[[1,3]] = 1
# In: b
# Out:
# array([[7, 1],
#  [7, 1]])



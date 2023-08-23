import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 数组的修剪和压缩

#  clip方法返回一个修剪过的数组，
#  也就是将所有比给定最大值还大的元素全部设为给定的最大值，
#  而所有比给定最小值还小的元素全部设为给定的最小值。
a = np.arange(5)
print(a)
print(a.clip(1,2))

a = np.arange(4)
print(a)
print(a.compress(a > 2))

# 阶乘
b = np.arange(1,9)
print(b)
print("factorial", b.prod())

print("factorials", b.cumprod())

print("diff", np.diff(b))

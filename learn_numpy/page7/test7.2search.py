# 搜索
import datetime
import numpy as np

# NumPy中有多个函数可以在数组中进行搜索，如下所示。
#  argmax函数返回数组中最大值对应的下标。
# >>> a = np.array([2, 4, 8])
# >>> np.argmax(a)
# 2

#  nanargmax函数提供相同的功能，但忽略NaN值。
# >>> b = np.array([np.nan, 2, 4])
# >>> np.nanargmax(b)
# 2

#  argmin和nanargmin函数的功能类似，只不过换成了最小值。
#  argwhere函数根据条件搜索非零的元素，并分组返回对应的下标。
# >>> a = np.array([2, 4, 8])
# >>> np.argwhere(a <= 4)
# array([[0],
#  [1]])

#  searchsorted函数可以为指定的插入值寻找维持数组排序的索引位置。该函数使用二分
# 搜索算法，计算复杂度为O(log(n))。

#  extract函数返回满足指定条件的数组元素。

# 使用 searchsorted 函数
# searchsorted函数为指定的插入值返回一个在有序数组中的索引位置，
# 从这个位置插入可以保持数组的有序性。

a = np.arange(5)
indices = np.searchsorted(a, [-2, 7])
print("Indices", indices)
print("The full array", np.insert(a, indices, [-2, 7]))

# 抽取元素
a = np.arange(7)
condition = (a % 2) == 0

print("Even numbers", np.extract(condition, a))
# 使用extract函数基于生成的条件从数组中抽取元素：
print("Non zero", np.nonzero(a))
# 使用nonzero函数抽取数组中的非零元素：


# 使用NumPy中的frompyfunc函数，通过一个Python函数来创建通用函数
import numpy as np


def ultimate_answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    return result


ufunc = np.frompyfunc(ultimate_answer, 1, 1)
print("the answer", ufunc(np.arange(4)))
print("The answer", ufunc(np.arange(4).reshape(2, 2)))
# 通用函数方法
# 通用函数并非真正的函数，而是能够表示函数的对象。

# 在 add 上调用通用函数的方法
a = np.arange(9)
print(a)
print("Reduce", np.add.reduce(a))
# 沿着指定的轴，在连续的数组元素之间递归调用通用函数，即可得到输入数组的规约
# （reduce）计算结果。对于add函数，其对数组的reduce计算结果等价于对数组元素求和。

# accumulate方法同样可以递归作用于输入数组。但是与reduce方法不同的是，
# 它将存储运算的中间结果并返回。因此在add函数上调用accumulate方法，
# 等价于直接调用cumsum函数。
print("Accumulate\n", np.add.accumulate(a))
print(np.cumsum(a))

# 输出0-5,2,2-7,7-结束的之和
print("Reduceat\n", np.add.reduceat(a, [0, 5, 2, 7]))


# outer方法返回一个数组，它的秩（rank）等于两个输入数组的秩的和。
# 它会作用于两个输入数组之间存在的所有元素对。
print("Outer", np.add.outer(np.arange(10), a))










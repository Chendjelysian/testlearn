# 数组运算
import numpy as np

# 除法
a = np.array([2, 6, 5])
b = np.array([1, 2, 3])

# 在python3里，divide、true_divide没有差别了
# 都是返回除法的浮点数结果而不作整数处理。
print("Divide", np.divide(a, b), np.divide(b, a))

print("Divide", np.true_divide(a, b), np.true_divide(b, a))
# 相当于先调用divide函数再调用floor函数。
# floor函数将对浮点数进行向下取整并返回整数
print("floor divide", np.floor_divide(a, b), np.floor_divide(a, b))
c = 3.14*b
print("floor divide2", np.floor_divide(c, b), np.floor_divide(b, c))

print(a/b)
print(a//b)

# 模运算

a = np.arange(-4,4)
print(a)
# 三个操作一样
print("remainder\n", np.remainder(a, 2))
print("remainder", np.mod(a, 2))
print("remainder", a % 2)

# 也是mod 但带正负
print("fmod", np.fmod(a, 2))

# 斐波那契数列
# 斐波那契数列的递推关系可以用矩阵来表示。斐波那契数列的计算等价于矩阵的连乘。

F = np.matrix([[1, 1], [1, 0]])
print(F)

# 计算斐波那契数列中的第8个数，即矩阵的幂为8减去1。
# 计算出的斐波那契数位于矩阵的对角线上
print((F ** 2))
print((F ** 3))
print((F ** 4))
print((F ** 5))
print((F ** 7)[0, 0])

# 斐波那契数列方案二
# 利用黄金分割公式或通常所说的比奈公式（Binet’ s Formula），
# 加上取整函数，就可以计算斐波那契数。

n = np.arange(1, 9)
sqrt5 = np.sqrt(5)
print(sqrt5)
phi = (1 + sqrt5)/2
fibonacci = np.rint((phi**n - (-1/phi)**n)/sqrt5)
print("Fibonacci", fibonacci)









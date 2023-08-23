
import numpy as np
import matplotlib.pyplot as plt

#
# 绘制一个多项式函数，
# 以及使用derive函数和参数m为1得到的其一阶导函数

# deriv([m])表示求导，参数m表示求几次导数
# integ([m,k])表示积分，参数m表示积几次分，k表示积分后的常数项的值

func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
func1 = func.deriv(m=1)
x = np.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)
plt.plot(x, y, 'rp', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 绘制多项式函数及其导函数

func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 30)
y = func(x)
func1 = func.deriv(m=1)
y1 = func1(x)
func2 = func.deriv(m=2)
y2 = func2(x)
# 使用subplot函数创建第一个子图。该函数的第一个参数是子图的行数，第二个参数
# 是子图的列数，第三个参数是一个从1开始的序号
# 另一种方式是将这3个参数结合成一个数字，如311。这样，子图将被组织成3行1列。
# 设置子图的标题为Polynomial，使用红色实线绘制。
plt.subplot(311)
plt.plot(x, y, 'r-')
plt.title("ploynomial")

plt.subplot(312)
plt.plot(x, y1, 'b^')
plt.title("first derivaive")

plt.subplot(313)
plt.plot(x, y2, 'go')
plt.title("second derivative")

plt.xlabel('x')
plt.ylabel('y')
plt.show()


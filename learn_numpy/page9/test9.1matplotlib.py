# matplotlib.pyplot包中包含了简单绘图功能。需要记住的是，
# 随后调用的函数都会改变当前的绘图。

# 使用NumPy的多项式函数poly1d来创建多项式。
import numpy as np
import matplotlib.pyplot as plt

# variable=‘z’表示改变未知数的字母
# 参数2：若参数2为True，则表示把数组中的值作为根，然后反推多项式，例如：
q = np.poly1d([2, 3, 5, 7], True, variable='z')
print(q)
# 表示当x = 0.5时，多项式的值为多少
print(q(1))
# q.r表示当多项式为 0 时，此等式的根
print(q.r)
# q.c表示生成多项式的系数数组
print(q.c)
# q.order表示返回最高项的次方数
print(q.order)
# q[1]表示返回第一项的系数
print(q[1])

func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 30)
y = func(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()

# 图表保存到本地图片文件
plt.savefig('多项式函数.png', bbox_inches='tight')
# 在三维空间中绘图
# 我们将在三维空间中绘制一个简单的三维函数。

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

import matplotlib.animation as animation

fig = plt.figure()
# 使用3d关键字来指定图像的三维投影
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(-1, 1, 100)
# 使用meshgrid函数创建一个二维的坐标网格。这将用于变量x和y的赋值
x, y = np.meshgrid(u, u)

z = x ** 2 + y ** 2
# 将指定行和列的步幅，以及绘制曲面所用的色彩表（color map）。
# 步幅决定曲面上“瓦片”的大小，而色彩表的选择取决于个人喜好。
ax.plot_surface(x, y, z, rstride=3, cstride=3, cmap=cm.YlGnBu_r)

plt.show()

# 等高线图
# Matplotlib中的等高线3D绘图有两种风格——填充的和非填充的。
# 我们可以使用contour函数创建一般的等高线图。
# 对于色彩填充的等高线图，可以使用contourf绘制。

fig = plt.figure()
ax = fig.add_subplot(111)
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
ax.contourf(x, y, z)
plt.show()

# 动画

fig = plt.figure()
ax = fig.add_subplot(111)
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)
circles, triangles, dots = ax.plot(x, 'ro', y, 'g^', z, 'b.')
ax.set_ylim(0, 1)
plt.axis('off')


def update(data):
    circles.set_ydata(data[0])
    triangles.set_ydata(data[1])
    return circles, triangles


def generate():
    while True: yield np.random.rand(2, N)


anim = animation.FuncAnimation(fig, update, generate, interval=150)
plt.show()

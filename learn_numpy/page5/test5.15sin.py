# 数组运算
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys
# 绘制利萨茹曲线

a = float(9)
b = float(8)
t = np.linspace(-np.pi, np.pi, 201)
x = np.sin(a * t + np.pi/2)
y = np.sin(b * t)
plot(x, y)
show()

# 方波

t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(100))
k = 2 * k - 1
f = np.zeros_like(t)
for i in range(len(t)):
 f[i] = np.sum(np.sin(k * t[i])/k)
f = (4 / np.pi) * f
plot(t, f)
show()
# 三角波
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(100))
f = np.zeros_like(t)
for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i])/k)
f = (-2 / np.pi) * f
plot(t, f, lw=1.0)
plot(t, np.abs(f), lw=2.0)
show()





# 我们将以一些专用数学函数结束本章的内容。贝塞尔函数（Bessel function）是
# 贝塞尔微分方程的标准解函数（详见http://en.wikipedia.org/wiki/Bessel_function）。
# 在NumPy中，以i0 表示第一类修正的零阶贝塞尔函数。sinc函数在NumPy中有同名函数sinc，
# 并且该函数也有一个二维版本。sinc是一个三角函数，
# 更多详细内容请访问http://en.wikipedia.org/wiki/Sinc_function。

import numpy as np

from matplotlib.pyplot import plot, show, legend, imshow
from matplotlib.dates import datestr2num

# 绘制修正的贝塞尔函数

x = np.linspace(0, 4, 100)
vals = np.i0(x)
plot(x, vals)
show()

# sinc函数在数学和信号处理领域被广泛应用。NumPy中有同名函数sinc，
# 并且也存在一个二维版本。

x = np.linspace(0, 4, 100)
vals = np.sinc(x)
plot(x, vals)
show()

x = np.linspace(0, 6, 100)
xx = np.outer(x, x)
vals = np.sinc(xx)
imshow(vals)
show()


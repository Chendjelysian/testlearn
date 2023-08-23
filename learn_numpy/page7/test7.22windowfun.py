# 窗函数（window function）是信号处理领域常用的数学函数，
# 相关应用包括谱分析和滤波器设计等。
# 这些窗函数除在给定区间之外取值均为0。
# NumPy中有很多窗函数，如bartlett、blackman、hamming、hanning和kaiser。
import numpy as np

from matplotlib.pyplot import plot, show, legend
from matplotlib.dates import datestr2num

window = np.bartlett(42)
plot(window)
show()

# 克莱曼窗
closes = np.loadtxt('D:\STU_DJ\PycharmProjects\pythonProject\learn_numpy\page7\data.csv', delimiter=',', usecols=(6,),
                    converters={1: datestr2num}, unpack=True)
N = int(2)
window = np.blackman(N)
smoothed = np.convolve(window / window.sum(), closes, mode='same')
plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()

# 我们来绘制汉明窗。

window = np.hamming(72)
plot(window)
show()

# 凯泽窗（Kaiser window）是以贝塞尔函数（Bessel function）定义的

window = np.kaiser(42,10)
plot(window)
show()


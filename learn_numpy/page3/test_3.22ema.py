# 指数移动平均线（exponential moving average）
# 指数移动平均线使用的权重是指数衰减的。对历史上的数据点
# 赋予的权重以指数速度减小，但永远不会到达
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

x = np.arange(5)
print("EXP", np.exp(x))

# linspace ,起始，终止，元素分段数量
print("Linspace", np.linspace(-1, 0, 5))

N = int(5)
weights = np.exp(np.linspace(-1. , 0. , N))

# 对权重值做归一化处理。我们将用到ndarray对象的sum方法。
weights /= weights.sum()
print("Weights", weights )

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, ema, lw=2.0)
show()
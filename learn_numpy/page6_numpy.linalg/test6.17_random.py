import numpy as np
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt

# 硬币赌博游戏
cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size=len(cash))

for i in range(1, len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
        cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError("Unexpected outcome " + outcome)
print(outcome.min(), outcome.max())

plot(np.arange(len(cash)), cash)
show()

# 超几何分布
# 超几何分布（hypergeometric distribution）是一种离散概率分布，它描述的是一个罐子里有
# 两种物件，无放回地从中抽取指定数量的物件后，抽出指定种类物件的数量。NumPy random模
# 块中的hypergeometric函数可以模拟这种分布。

# (使用hypergeometric函数初始化游戏的结果矩阵。该函数的第一个参数为罐中普通球
# 的数量，第二个参数为“倒霉球”的数量，第三个参数为每次采样（摸球）的数量。

points = np.zeros(100)
outcomes = np.random.hypergeometric(25, 1, 3, size=len(points))
# (2) 根据上一步产生的游戏结果计算相应的得分。
for i in range(len(points)):
    if outcomes[i] == 3:
        points[i] = points[i - 1] + 1
    elif outcomes[i] == 2:
        points[i] = points[i - 1] - 6
    else:
        print(outcomes[i])
# (3) 使用Matplotlib绘制points数组。
plot(np.arange(len(points)), points)
show()

# 连续分布可以用PDF（Probability Density Function，概率密度函数）来描述。
# 随机变量落在某一区间内的概率等于概率密度函数在该区间的曲线下方的面积。
# NumPy的random模块中有一系列连续分布的函数——beta、chisquare、exponential、
# f、gamma、gumbel、laplace、lognormal、logistic、multivariate_normal、
# noncentral_chisquare、noncentral_f、normal等。

# 绘制正态分布


N = 1000000
normal_values = np.random.normal(size=N)
dummy, bins, list1 = plt.hist(normal_values, int(np.sqrt(N)), rwidth=1 )
sigma = 1
mu = 0
plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), lw=2)
plt.show()

# 对数正态分布
# 对数正态分布（lognormal distribution） 是自然对数服从正态分布的任意随机变量的概率分
# 布。NumPy random模块中的lognormal函数模拟了这个分布。


N=1000000
lognormal_values = np.random.lognormal(size=N)

dummy, bins, dummy = plt.hist(lognormal_values, int(np.sqrt(N)), rwidth=1)
sigma = 1
mu = 0
print(np.sqrt(N))
x = np.linspace(min(bins), max(bins), len(bins))
pdf = np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))/ (x * sigma * np.sqrt(2 * np.pi))
plt.plot(x, pdf,lw=3)
plt.show()
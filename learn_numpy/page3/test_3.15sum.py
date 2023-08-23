# 周汇总

import numpy
import numpy as np
import datetime

o, c, v = np.loadtxt('data.csv', delimiter=',', usecols=(3, 6, 7), unpack=True)

print(c)

# 加权平均
vwap = np.average(c, weights=v)
print("vwap = ", float(vwap))
# 算数平均
print("算术平均", np.mean(c))

# 3.8 min and max

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)

print("highest =", np.max(h))
print("lowest =", np.min(l))

print("Spread high price", np.ptp(h))

print("Spread low price", np.ptp(l))

# 3.10 简单统计分析
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print("median =", np.median(c))

sorted1 = np.sort(c, axis=0)
print("sorted =", sorted1)

N = len(c)
print("middle =", sorted1[int((N - 1) / 2)])
print("average middle =", (sorted1[int(N / 2)] + sorted1[int((N - 1) / 2)]) / 2)

# 方差
print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean()) ** 2))
# NumPy中的diff函数可以返回一个
# 由相邻数组元素的差值构成的数组


# 简单收益率
returns = np.diff(c) / c[:-1]
print("Standard deviation =", np.std(returns))
# 对数收益率
logreturns = np.diff(np.log(c))
print(logreturns)
# 收益率为正值
posretindices = np.where(returns > 0)
print("Indices with positive returns", posretindices)

# 波动率（volatility）是对价格变动的一种度量。
# 历史波动率可以根据历史价格数据计算得出。
# 计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率。
# 年波动率等于对数收益率的标准差除以其均值

annual_volatility = np.std(logreturns) / np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print(annual_volatility)


# 分析日期数据

# 转换函数

# 星期一 0
# 星期二 1
# 星期三 2
# 星期四 3
# 星期五 4
# 星期六 5
# 星期日 6
def datestr2num(s):
    d = datetime.datetime.strptime(s.decode('ascii'), "%d-%m-%Y")
    return d.date().weekday()


dates, close = np.loadtxt('data.txt', delimiter=',', usecols=(1, 6), converters={1: datestr2num}, unpack=True)
print("Dates =", dates)

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print("Day", i, "prices", prices, "Average", avg)
    averages[i] = avg

top = np.max(averages)
print("highest average", top)

# 汇总
close = close[:10]
dates = dates[:10]

# 找第一个周一
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is", first_monday)

# 找最后一个周五
last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is", last_friday)

# 接下来创建一个数组，用于存储三周内每一天的索引值。

weeks_indices = np.arange(first_monday, last_friday + 1)
print("Weeks indices initial", weeks_indices)

# 按照每个子数组5个元素，用split函数切分数组：
weeks_indices = np.split(weeks_indices, 1)
print("Weeks indices after split", weeks_indices)


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return ("APPL", monday_open, week_high, week_low, friday_close)


weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, o, h, l, close)

print("Week summary", weeksummary)

np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")

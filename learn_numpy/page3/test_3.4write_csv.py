import numpy
import numpy as np
import datetime

c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

print(c)

# 加权平均
vwap = np.average(c, weights=v)
print("vwap = ", float(vwap))
# 算数平均
print("算术平均", np.mean(c))

# import numpy as np
# a=np.arange(15).reshape(3,5)
# print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
# print(np.sum(a))   #对数组内所有元素求和
# 105
# print(np.sum(a,axis=0))
# [15 18 21 24 27]
# #对数组内行列求和，axis=0，数组列求和，axis=1，数组行求和
# print(np.sum(a,axis=1))
# [10 35 60]
# print(np.average(a))        #对数组内所有元素求平均值
# 7.0
# print(np.average(a,axis=0))        #对数组内列进行加权平均
# [5. 6. 7. 8. 9.]
# print(np.average(a,axis=1))        #对数组内行进行加权平均
# [ 2.  7. 12.]
# print(np.std(a))        #对数组求标准差
# 4.320493798938574
# print(np.std(a,axis=0))        #对数组的列求标准差
# [4.0824829 4.0824829 4.0824829 4.0824829 4.0824829]
# print(np.std(a,axis=1))        #对数组的行求标准差
# [1.41421356 1.41421356 1.41421356]
#
# print(np.var(a))            #对数组进行求方差
# 18.666666666666668
# print(np.var(a,axis=0))            #对数组的列进行求方差
# [16.66666667 16.66666667 16.66666667 16.66666667 16.66666667]
# print(np.var(a,axis=1))            #对数组的行进行求方差
# [2. 2. 2.]


a = np.random.randint(1, 100, (3, 4))
print(a)
# [[42 11  9 84]
#  [57 94 64 93]
#  [85  3 41 38]]
# print(np.max(a))  #数组中最大值
# 94
# print(np.min(a))       #数组中的最小值
# 3
# print(np.argmax(a))     #返回数组扁平化之后，最大值的下标
# 5
# print(np.argmin(a))     #返回数组扁平化之后，最小值的下标
# 9
# print(np.unravel_index(np.argmax(a),(2,6)))  #将a扁平化后的最大值小标，转化为结构为（2,6）的下标。
# (0, 5)
#
# print(np.ptp(a))            #返回最大值与最小值的差
# 91
# print(np.median(a))     #返回数组a中元素的中位数（中值）
# 49.5


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


a = [11, 12, 14, 15, 17, 12, 15, 16, 30, 24]
# 简单收益率
returns = np.diff(a) / a[:-1]
print("Standard deviation =", np.std(returns))
# 对数收益率
logreturns = np.diff(np.log(a))
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

import numpy as np
from matplotlib.dates import DateFormatter 
from matplotlib.dates import DayLocator 
from matplotlib.dates import MonthLocator 
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from pylab import mpl

# 设置中文显示字体
mpl.rcParams["font.sans-serif"] = ['Microsoft YaHei']
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# (2) 我们需要创建所谓的定位器（locator），这些来自
# matplotlib.dates包中的对象可以在x轴上定位月份和日期。
# alldays = DayLocator()
# months = MonthLocator()

# (3) 创建一个日期格式化器（date formatter）以格式化x轴上的日期。
# 该格式化器将创建一个字符串，包含简写的月份和年份。
# month_formatter = DateFormatter("%b %Y")

# (4) 从雅虎财经频道下载股价数据。
# quotes = quotes_historical_yahoo(symbol, start, today)

# (5) 创建一个Matplotlib的figure对象——这是绘图组件的顶层容器。
# fig = plt.figure()

# (6) 增加一个子图。
# ax = fig.add_subplot(111)

# (7) 将x轴上的主定位器设置为月定位器。该定位器负责x轴上较粗的刻度。
# ax.xaxis.set_major_locator(months)

# (8) 将x轴上的次定位器设置为日定位器。该定位器负责x轴上较细的刻度。
# ax.xaxis.set_minor_locator(alldays)

# (9) 将x轴上的主格式化器设置为月格式化器。该格式化器负责x轴上较粗刻度的标签。
# ax.xaxis.set_major_formatter(month_formatter)

# (10) matplotlib.finance包中的一个函数可以绘制K线图。这样，我们就可以使用获取的
# 股价数据来绘制K线图。我们可以指定K线图的矩形宽度，现在先使用默认值。
# candlestick(ax, quotes)

# (11) 将x轴上的标签格式化为日期。为了更好地适应x轴的长度，标签将被旋转。
# fig.autofmt_xdate()
# plt.show()


# plt.hist

#函数功能：判定数据(或特征)的分布情况
# 调用方法：plt.hist(x, bins=10, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False)
# 参数说明：
# x：指定要绘制直方图的数据；
# bins：指定直方图条形的个数；
# range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；
# density：是否将直方图的频数转换成频率；
# weights：该参数可为每一个数据点设置权重；
# cumulative：是否需要计算累计频数或频率；
# bottom：可以为直方图的每个条形添加基准线，默认为0；
# histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’, ‘stepfilled’；
# align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
# orientation：设置直方图的摆放方向，默认为垂直方向；
# rwidth：设置直方图条形宽度的百分比；
# log：是否需要对绘图数据进行log变换；
# color：设置直方图的填充色；
# label：设置直方图的标签，可通过legend展示其图例；
# stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放；


# 多组数据直方图
data = np.random.randn(1000, 2)

plt.hist(x=data,  # 绘图数据
         bins=20,  # 指定直方图的条形数为20个
         edgecolor='w',  # 指定直方图的边框色
         color=['c', 'r'],  # 指定直方图的填充色
         label=['第一组', '第二组'],  # 为直方图呈现图例
         density=False,  # 是否将纵轴设置为密度，即频率
         alpha=0.6,  # 透明度
         rwidth=1,  # 直方图宽度百分比：0-1
         stacked=False)  # 当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放

ax = plt.gca()  # 获取当前子图
ax.spines['right'].set_color('none')  # 右边框设置无色
ax.spines['top'].set_color('none')  # 上边框设置无色
# 显示图例
plt.legend()
# 显示图形
plt.show()


# 绘制累计频率直方图：通过参数cumulative = True绘制
data = np.random.randn(1000)
plt.hist(data,  # 绘图数据
         bins=20,  # 指定直方图的组距
         density=True,  # 设置为频率直方图
         cumulative=True,  # 积累直方图
         color='steelblue',  # 指定填充色
         edgecolor='w',  # 指定直方图的边界色
         label='直方图')  # 为直方图呈现标签

# 设置坐标轴标签和标题
plt.title('累计频率直方图')
plt.xlabel('x轴')
plt.ylabel('累计频率')

# 显示图例
plt.legend(loc='best')
# 显示图形
plt.show()

# 密度图（频率图）：密度图经常跟直方图一起使用，而在matplotlib中没有单独绘制密度图的函数，笔者目前知道两种绘制密度图的方法：
#
# 1）通过pandas(数据分析与统计模块)，将数据转换成series或dataframe，然后绘图:

x = np.random.randn(1000)
data = pd.Series(x)  # 将数据由数组转换成series形式
plt.hist(data, density=True, edgecolor='w', label='直方图')
data.plot(kind='kde', label='密度图')

# 显示图例
plt.legend()
# 显示图形
plt.show()


# 对数坐标plt.semilogy(dates, volume)

SNR = [0, 5 ,10, 15, 20, 25, 30]
result = [0.15, 0.08, 0.03, 0.015, 0.005, 0.001, 0.0008]
plt.semilogy(result, 'm--v', label='SNR-BER')  # 对 result 取 log 后画线
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("log-line")
plt.legend(loc=0)
plt.grid(True)  # 显示网格线
# 给特定的点打标签
# 对于特殊的点，想标记出其对应的值，可以使用 plt.text(a, b, val, color='r') 函数。
plt.text(SNR[3], result[3], result[3], color='r')  # 标注第 4 个点的值
plt.show()

# 散点图

# scatter(x, y, s=None, c=None,
#       marker=None, cmap=None, norm=None, vmin=None, vmax=None,
#       alpha=None, linewidths=None, *, edgecolors=None,
#       plotnonfinite=False, data=None, **kwargs)

SNR = [0, 5, 10, 15, 20, 25, 30]
result = [0.15, 0.08, 0.03, 0.015, 0.005, 0.001, 0.0008]
# 散点图
plt.scatter(SNR, result, marker='v', color='b', label='SNR-BER')
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("log-line")
plt.legend(loc=0)
plt.grid(True)  # 显示网格线
plt.show()


# 画矩阵
# 可以使用 matplotlib.pyplot.matshow() 函数绘制二维矩阵的图像。
#
# 这一般在矩阵可视化的时候用的比较多。另外可以使用 colorbar() 函数设置显示颜色标记。


# 自定义坐标轴显示内容 xticks()/yticks()
# 如果坐标轴想用其他字符显示，可以使用 xticks() / yticks() 函数。
# 函数第一个参数是原来的坐标显示列表，第二个参数是实际的显示字符。

# 创建对角矩阵
a = np.diag(range(5))
fig = plt.matshow(a)
# 显示颜色标记
plt.colorbar(fig.colorbar, fraction=0.2)
# 自定义 y 轴显示内容
plt.yticks(range(5),
           ['A', 'B', 'C', 'D', 'E'])
plt.show()


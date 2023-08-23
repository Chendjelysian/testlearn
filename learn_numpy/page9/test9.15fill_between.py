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

# (4) 对收盘价下方的区域进行着色，依据低于或高于平均收盘价使用不同的颜色填充。
# plt.fill_between(dates, close.min(), close,
#  where=close>close.mean(), facecolor="green", alpha=0.4)
# plt.fill_between(dates, close.min(), close,
#  where=close<close.mean(), facecolor="red", alpha=0.4)




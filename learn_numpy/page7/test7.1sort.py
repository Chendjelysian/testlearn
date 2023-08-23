# 排序
import datetime

import numpy as np


# NumPy提供了多种排序函数，如下所示：
#  sort函数返回排序后的数组；
#  lexsort函数根据键值的字典序进行排序；
#  argsort函数返回输入数组排序后的下标；
#  ndarray类的sort方法可对数组进行原地排序；
#  msort函数沿着第一个轴排序；
#  sort_complex函数对复数按照先实部后虚部的顺序进行排序。

# 按字典序排序

def datestr2num(s):
    return datetime.datetime.strptime(s.decode('ascii'), "%d-%m-%Y").toordinal()


dates, closes = np.loadtxt('data.csv', delimiter=',',
                           usecols=(1, 6), converters={1: datestr2num}, unpack=True)

indices = np.lexsort((dates, closes))

print("Indices", indices )

print(["%s %s" % (datetime.date.fromordinal(int(dates[i])),
                  closes[i]) for i in indices])

# 对复数进行排序

np.random.seed(42)
complex_numbers = np.random.random(5) + 1j * np.random.random(5)
print("Complex numbers\n", complex_numbers)

print("Sorted\n", np.sort_complex(complex_numbers))
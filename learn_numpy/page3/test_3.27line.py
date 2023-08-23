# fill函数可以将数组元素的值全部设置为一个指定的标量值，
# 它的执行速度比使用array.flat = scalar或者用循环遍历数组赋值的方法更快。
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)
pivots = (h + l + c ) / 3

print("pivots", pivots)


def fit_line(t, y):
    A = np.vstack([t, np.ones_like(t)]).T
    return np.linalg.lstsq(A, y, rcond= None)[0]


t = np.arange(len(c))
sa, sb = fit_line(t, pivots - (h - l))
ra, rb = fit_line(t, pivots + (h - l))
support = sa * t + sb
resistance = ra * t + rb

condition = (c > support) & (c < resistance)
print("Condition", condition)
between_bands = np.where(condition)

between_bands = len(np.ravel(between_bands))
print("Number points between bands", between_bands)
print("Ratio between bands", float(between_bands)/len(c))

print("Tomorrows support", sa * (t[-1] + 1) + sb )
print ("Tomorrows resistance", ra * (t[-1] + 1) + rb )
a1 = c[c > support]
a2 = c[c < resistance]
print( "Number of points between bands 2nd approach" ,len(np. intersect1d(a1, a2)) )


plot(t, c)
plot(t, support)
plot(t, resistance)
show()
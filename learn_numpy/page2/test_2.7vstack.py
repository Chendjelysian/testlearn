import numpy
import numpy as np

a = np.arange(9).reshape(3, 3)

print(a)

b = 2 * a
print(b)
# 水平组合
print(np.hstack((a, b)))
print(np.concatenate((a,b), axis=1))
# 垂直组合
print(np.vstack((a, b)))
print(np.concatenate((a,b), axis=0))
# 深度组合
print( np.dstack((a, b)) )


# 列组合

oned = np.arange(2)
print(oned)
twice_oned = 2 * oned
print(twice_oned)

print(np.column_stack((oned, twice_oned)))

print(np.column_stack((a, b)) )

# 行组合

print(np.row_stack((oned, twice_oned)))
print(np.column_stack((a, b)))
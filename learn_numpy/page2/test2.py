import numpy
import numpy as np

a = numpy.array(2)
print(a)

b = np.arange(24).reshape(2, 3, 4)
print(b.shape)
print(b)
print("\n")
print(b[0, 0, 0])
print(b[:, 0, 0])
print(b[0, :, :])
print("b[0, ...]:")
print(b[0, ...])
print("b[:, 1]:")
print(b[:, 1])

print(" b[0,::-1, -1]: \n")
print(b[0, ::-1, -1])
print("b[0,::2,-1] ：")
print(b[0, ::2, -1])

print(b[::-1])

print(b[:, -1, -1])


import numpy as np
from matplotlib.pyplot import plot, show


x = np.linspace(0, 2 * np.pi, 30)
wave = np.sin(x)
transformed = np.fft.fft(wave)

print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9))
plot(transformed)
show()

# 移频
# numpy.linalg模块中的fftshift函数可以将FFT输出中的直流分量移动到频谱的中央。
# ifftshift函数则是其逆操作。

x = np.linspace(0, 2 * np.pi, 100)
wave = np.cos(x)
transformed = np.fft.fft(wave)
shifted = np.fft.fftshift(transformed)

print(np.fft.fftshift(transformed))
print(np.all(np.abs(np.fft.ifftshift(shifted) - transformed) < 10 ** -9) )
plot(transformed, lw=2)
plot(shifted, lw=3)
show()



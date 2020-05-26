import random
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import exp,sin,cos
from scipy.fftpack import fft,ifft
from matplotlib.ticker import FuncFormatter
f1 = 0.1
f2 = 0.25
pi = math.pi
n_start = 0
n_end = 256
n_s = 1
N = n_end
n = np.arange(n_start,n_end,n_s)
x_n = 10*sin(2*pi*f1 * n + pi/3) + 2*sin(2*pi*f2 * n + pi/4) + np.random.randn(n.size) #在原始信号中加上噪声
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20, 28))
plt.subplot(511)
for i in range(n_start,n_end):
    plt.plot([i,i],[0,x_n[i]],color='b')
plt.title('实信号')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.scatter(n,x_n,marker='o')
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
X_n = fft(x_n)
abs_X_n = np.abs(X_n)
PSD1 = abs_X_n**2 / (n_end+1)
def to_percent(temp, position):
    return '%.1f' % (temp/256)
plt.figure(figsize=(10, 28))
plt.subplot(5,1,1)
plt.plot(abs_X_n)
for i in range(n_start,n_end):
    plt.plot([i,i],[0,abs_X_n[i]],color='b')
plt.title('x(n)的FFT')
plt.xlabel('n')
plt.ylabel('Xn(w)')
plt.scatter(n,abs_X_n,marker='o')
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')


plt.subplot(5,1,2)
plt.plot(PSD1)
for i in range(n_start,n_end):
    plt.plot([i,i],[0,PSD1[i]],color='b')
plt.title('周期图法求PSD')
plt.xlabel('f')
plt.ylabel('PSD')
plt.scatter(n,PSD1,marker='o')
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

plt.show()

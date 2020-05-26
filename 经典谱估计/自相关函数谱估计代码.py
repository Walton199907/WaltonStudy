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

def autocorr(x):
    result = np.correlate(x, x, mode='full')/N
    return result[result.size//2:]

n = np.arange(n_start,n_end,n_s)
x_n = 10*sin(2*pi*f1 * n + pi/3) + 2*sin(2*pi*f2 * n + pi/4) + np.random.randn(n.size) #在原始信号中加上噪声
cor_x_2 = autocorr(x_n)
PSD3 = fft(cor_x_2)
PSD3 = np.abs(PSD3)
plt.figure(figsize=(10, 28))
plt.subplot(511)
plt.plot(PSD3)
for i in range(n_start,n_end,n_s):
    plt.plot([i,i],[0,PSD3[i]],color='b')
plt.title('自相关法法求PSD')
plt.xlabel('f')
plt.ylabel('PSD')
plt.scatter(n,PSD3,marker='o')
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
def to_percent(temp, position):
    return '%.1f' % (temp/258)
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.show()

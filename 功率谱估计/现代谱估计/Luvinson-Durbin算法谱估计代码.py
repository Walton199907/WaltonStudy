import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma import exp,sin,cos,log10
import scipy.signal as signal
def findpeak(w,PSD,N,f1,f2):
    f=[]
    PSD_std=[0,0]
    pos = [0,0]
    for i in range(1,N-1):
        if PSD[i] > PSD[i-1] and PSD[i]>PSD[i+1]:
                if PSD[i]>PSD_std[0]:
                    if PSD[i]>PSD_std[1]:
                        if PSD_std[0]>=PSD_std[1]:
                            PSD_std[1] = PSD[i]
                            pos[1] = i
                        else:
                            PSD_std[0] = PSD[i]
                            pos[0] = i
                    else:
                        PSD_std[0] = PSD[i]
                        pos[0] = i
                else:
                    if PSD[i]>PSD_std[1]:
                        PSD_std[1] = PSD[i]
                        pos[1] = i          
    f.append(w[pos[0]]/(2*pi))
    f.append(w[pos[1]]/(2*pi))
    return f

def autocorr(x):
    result = np.correlate(x, x, mode='full')/N
    return result[result.size//2:]
f1 = 0.1
f2 = 0.25
pi = math.pi
N=256
p = 50
n = np.arange(0,N,1) 
x_n = 10*sin(2*pi*f1 * n + pi/3) + 2*sin(2*pi*f2 * n + pi/4) + np.random.randn(n.size) #在原始信号中加上噪声
a = np.zeros((p,p))  #a为p*p维的数组
p0 = 0
Rx = autocorr(x_n)
for i in range(0,N):
    p0 += x_n[i]**2
p0 = p0/N
a[0,0] = -Rx[1]/Rx[0]
P = [p0]
k = [a[0,0]]
P1 = p0*(1-k[0]**2)
P.append(P1)
for m in range(2,p+1):
    ka = 0 #反向系数的分子
    kb = 0 #反向系数的分母 
    for i in range(1,m):
        ka += a[m-2,i-1]*Rx[m-i]
    ka += Rx[m]
    kb = -P[m-1]
    k.append(ka/kb)
    a[m-1,m-1] = ka/kb
    for i in range(1,m):
        a[m-1,i-1] = a[m-2,i-1]+k[m-1]*a[m-2,m-i-1]
    P.append(P[m-1]*(1-k[m-1]**2))
hb=[1]
for i in range(0,p):
    hb.append(a[p-1,i])
#把0阶的最小预测误差功率从P[]中删除
P.remove(P[0])
ha=[1]
w,H = signal.freqz(ha,hb)
G_2 = P[p-1]
PSD = G_2*((np.abs(H))**2)
PSD1 = 10*log10(PSD)
plt.figure(figsize=(10, 28))
plt.subplot(511)
plt.plot(x_n)
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')

plt.subplot(512)
plt.plot(w/(2*pi),abs(PSD1))
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')

f = findpeak(w,PSD1,N,f1,f2)
print(f)

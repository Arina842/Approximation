import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
y = [0, 3, 2, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

def once (x,y):
    tao = []
    epsilon = []
    i, k = 3, 0
    tao.append(0)
    epsilon.append(0)
    tao .append((x[0] + x[1] + x[2]) / 3)
    tao .append((x[0] + x[1] + x[2] + x[3]) / 4)
  
    while i < (len(x)-3):
        k = (x[i-2]+x[i-1]+x[i]+x[i+1]+x[i+2])/5
        tao.append(k)
        i += 1
    tao.append((x[-4] + x[-3] + x[-2]+x[-1]) / 4)
    tao .append((x[-3] + x[-2] + x[-1]) / 3)
    tao .append(( x[-2] + x[-1]) / 2)

    epsilon.append((y[0] + y[1] + y[2]) / 3)
    epsilon.append((y[0] + y[1] + y[2] + y[3]) / 4)
    i=3
  
    while i < (len(y)-3):
        k = (y[i-2]+y[i-1]+y[i]+y[i+1]+y[i+2])/5
        epsilon.append(k)
        i += 1
      
    epsilon.append((y[-4] + y[-3] + y[-2]+y[-1]) / 4)
    epsilon.append((y[-3] + y[-2] + y[-1]) / 3)
    epsilon.append((y[-2] + y[-1]) / 2)
    return tao, epsilon

d, f = once(x, y)
r, t = once(d, f)
v, b = once(r, t)
p, o = once(v, b)
print(*p,*o , end=',,,')
p.append(p[-1] + ((p[-1] - p[-2])+(p[-2] - p[-3])+(p[-3] - p[-4])+(p[-4] - p[-5]))/3)
o.append(o[-1] + ((o[-1] - o[-2])+(o[-2] - o[-3])+(o[-3] - o[-4])+(o[-4] - o[-5]))/3)
plt.plot(p, o)

maxX = np.max(x)
minX = np.min(x)
maxY = np.max(y)
minY = np.min(y)
print('maxX =', maxX, 'maxY =', maxY, 'minX =', minX, 'minY =', minY)
plt.plot(x, y)

plt.show()

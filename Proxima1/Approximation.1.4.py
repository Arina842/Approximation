import numpy as np
import matplotlib.pyplot as plt
from random import randint
from scipy import interpolate


plt.style.use('bmh')
x = [0]
y= [0]
for i in range(21):
    y.append(randint(1, 40))

x = np.linspace(0, 82, 22)
temp = interpolate.splrep(x, y)
xnew = np.arange(0, 82, 0.2)
ynew = interpolate.splev(xnew, temp)
plt.plot(xnew, ynew, linewidth=5)

minus_line_y = [0]
minus_line_x = [0]
plus_line_y = [0]
plus_line_x = [0]
i = 2
while i < (len(ynew)):
    if ynew[i - 2] < ynew[i - 1] and ynew[i - 1] > ynew[i]:
        plus_line_y.append(ynew[i - 1])
        plus_line_x.append(xnew[i - 1])
    elif ynew[i - 2] > ynew[i - 1] and ynew[i - 1] < ynew[i]:
        minus_line_y.append(ynew[i - 1])
        minus_line_x.append(xnew[i - 1])
    elif ynew[i - 1] == ynew[i]:
        if ynew[i - 2] > ynew[i - 1]:
            minus_line_y.append(ynew[i - 1])
            minus_line_x.append(xnew[i - 1])
        else:
            plus_line_y.append(ynew[i - 1])
            plus_line_x.append(xnew[i - 1])
    i += 1
minus_line_y.append(ynew[i - 1])
minus_line_x.append(xnew[i - 1])
plus_line_y.append(ynew[i - 1])
plus_line_x.append(xnew[i - 1])

plt.plot(minus_line_x,minus_line_y,linewidth= 1, linestyle='dashed',marker='o')
plt.plot(plus_line_x,plus_line_y,linewidth= 1, linestyle='dashed',marker='o')
plt.style.use('bmh')
def once (xnew,ynew):
    tao = []
    epsilon = []
    i, k = 3, 0
    tao.append(0)
    epsilon.append(0)
    tao .append((xnew[0] + xnew[1] + xnew[2]) / 3)
    tao .append((xnew[0] + xnew[1] + xnew[2] + xnew[3]) / 4)
    while i < (len(xnew)-3):
        k = (xnew[i-2]+xnew[i-1]+xnew[i]+xnew[i+1]+xnew[i+2])/5
        tao.append(k)
        i += 1
    tao.append((xnew[-4] + xnew[-3] + xnew[-2]+xnew[-1]) / 4)
    tao .append((xnew[-3] + xnew[-2] + xnew[-1]) / 3)
    tao .append((xnew[-2] + xnew[-1]) / 2)

    epsilon.append((ynew[0] + ynew[1] + ynew[2]) / 3)
    epsilon.append((ynew[0] + ynew[1] + ynew[2] + ynew[3]) / 4)
    i=3
    while i < (len(ynew)-3):
        k = (ynew[i-2]+ynew[i-1]+ynew[i]+ynew[i+1]+ynew[i+2])/5
        epsilon.append(k)
        i += 1

    epsilon.append((ynew[-4] + ynew[-3] +ynew[-2]+ynew[-1]) / 4)
    epsilon.append((ynew[-3] + ynew[-2] + ynew[-1]) / 3)
    epsilon.append((ynew[-2] + ynew[-1]) / 2)
    return tao, epsilon

d, f = once(x, y)
d.append(x[-1])
f.append((y[-1]))
r, t = once(d, f)
r.append((r[-1] + xnew[-1]) / 2)
t.append((f[-1] + ynew[-1]) / 2)
v, b = once(r, t)
v.append((v[-1] + xnew[-1]) / 2)
b.append((b[-1] + ynew[-1]) / 2)
p, o = once(v, b)
p.append((p[-1] + xnew[-1]) / 2)
o.append((o[-1] + ynew[-1]) / 2)
p.append(xnew[-1])
o.append(ynew[-1])
temp = interpolate.splrep(p, o)
pnew = np.arange(0, 82, 0.2)
onew = interpolate.splev(pnew, temp)
plt.plot(pnew, onew,linewidth= 1)

maxX = np.max(xnew)
minX = np.min(xnew)
maxY = np.max(ynew)
minY = np.min(ynew)
print('maxX =', maxX, 'maxY =', maxY, 'minX =', minX, 'minY =', minY)
plt.show()

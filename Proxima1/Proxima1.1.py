import numpy as np
import matplotlib.pyplot as plt
from random import randint


plt.style.use('bmh')
fig, ax = plt.subplots()
x = [0]
y = [0]
for i in range(21):
    y.append(randint(1, 10))
x = np.linspace(0, 82, 22)

plt.plot(x, y,linewidth= 3)
minus_line_y = [0]
minus_line_x = [0]
plus_line_y = [0]
plus_line_x = [0]

i = 2
while i < (len(y)):
    if y[i-2] < y[i-1] and y[i-1] > y[i]:
        plus_line_y.append(y[i-1])
        plus_line_x.append(x[i-1])
    elif y[i-2] > y[i-1] and y[i-1] < y[i]:
        minus_line_y.append(y[i-1])
        minus_line_x.append(x[i-1])
    elif y[i-1] == y[i]:
        if y[i-2] > y[i-1]:
            minus_line_y.append(y[i-1])
            minus_line_x.append(x[i-1])
        else:
            plus_line_y.append(y[i-1])
            plus_line_x.append(x[i-1])
    i += 1
minus_line_y.append(y[i-1])
minus_line_x.append(x[i-1])
plus_line_y.append(y[i-1])
plus_line_x.append(x[i-1])

plt.plot(minus_line_x,minus_line_y,linewidth= 1, linestyle='dashed',marker='o')
plt.plot(plus_line_x,plus_line_y,linewidth= 1, linestyle='dashed',marker='o')
plt.style.use('bmh')
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
    tao .append((x[-2] + x[-1]) / 2)

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
d.append(x[-1])
f.append((y[-1]))
r, t = once(d, f)
r.append((r[-1]+x[-1])/2)
t.append((f[-1]+y[-1])/2)
v, b = once(r, t)
v.append((v[-1]+x[-1])/2)
b.append((b[-1]+y[-1])/2)
p, o = once(v, b)

p.append((p[-1]+x[-1])/2)
o.append((o[-1]+y[-1])/2)
p.append(x[-1])
o.append(y[-1])

plt.plot(p, o,linewidth= 1)

maxX = np.max(x)
minX = np.min(x)
maxY = np.max(y)
minY = np.min(y)
print('maxX =', maxX, 'maxY =', maxY, 'minX =', minX, 'minY =', minY)

plt.show()


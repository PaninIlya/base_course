import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x0 = 0.1
y0 = 0.1
C = 0.3
D = 2
n = 200

def points():
    x = np.zeros(n)
    y = np.zeros(n)

    x[0]= x0
    y[0] = y0

    for i in range(1, n):
        x[i] = x[i-1]**2 - y[i-1]**2 + C
        y[i] = 2*x[i-1] * y[i-1] + D
    
    return x, y


x, y = points()

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
x_l, y_l = [], []
# frames_interval = np.linspace(0, 2*np.pi, 100)

x_min, x_max = x.min() - 0.1, x.max() + 0.1
y_min, y_max = y.min() - 0.1, y.max() + 0.1
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal') 



def anim(i):
    if i < n:
        x_l.append(x[i])
        y_l.append(y[i])
        anim_object.set_data(x_l, y_l)

    return anim_object


ani = FuncAnimation(fig, #Вызов пространства для анимации
                    anim,
                     frames = range(n), #Интервал значений
                     interval=50)#Интервал между кадрами , по умолчанию 200 милисекунд(в нашем случае 50 милисекунд)


ani.save('les7_task4.gif', writer = 'pillow')
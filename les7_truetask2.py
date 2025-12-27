import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
a = 1
t = np.arange(0, 4*np.pi, 0.01)
phi = np.arange(0, 2*np.pi, 0.1)
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)



# def circle(phi):
#     R = a*t
#     x = R * np.cos(phi)
#     y = R* np.sin(phi)
#     return x, y

# x1, y1 = [], []
ax.set_xlim(-20, 20)  
ax.set_ylim(-20, 20)  
ax.set_aspect('equal')


def update(frame):
    R = a*frame
    x = R * np.cos(phi)
    y = R* np.sin(phi)

    #Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, #Вызов пространства для анимации
                    update,
                     frames = t, #Интервал значений
                     interval=50)#Интервал между кадрами , по умолчанию 200 милисекунд(в нашем случае 50 милисекунд)


ani.save('les7_truetask2.gif', writer = 'pillow')
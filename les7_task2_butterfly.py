import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

t = np.arange(0, 12 * np.pi, 0.1)

# def batterfly():

#     x = np.sin(t)*(np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
#     y = np.cos(t)*(np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
#     return x, y


fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)  # запятая создает кортеж(/убирает)
x1, y1 = [], []  # Координаты объекта анимации
# frames_interval = np.linspace(0, 6*np.pi, 100)#параметр перебирается от 0 до 2 пи

ax.set_xlim(-5, 5)  # пределы изменения переменной x
ax.set_ylim(-5, 5)  # пределы изменения переменной y
ax.set_aspect('equal')


def update(t_cur):
    x2 = np.sin(t_cur) * (np.e ** np.cos(t_cur) - 2 * np.cos(4 * t_cur) + np.sin(t_cur / 12) ** 5)
    y2 = np.cos(t_cur) * (np.e ** np.cos(t_cur) - 2 * np.cos(4 * t_cur) + np.sin(t_cur / 12) ** 5)
    x1.append(x2)
    y1.append(y2)

    # Передача координат объекту анимации
    anim_object.set_data(x1, y1)

    return anim_object


ani = FuncAnimation(fig,  # Вызов пространства для анимации
                    update,
                    frames=t,  # Интервал значений
                    interval=50)  # Интервал между кадрами , по умолчанию 200 милисекунд(в нашем случае 50 милисекунд)

ani.save('les7_task2_butterfly.gif', writer='pillow')
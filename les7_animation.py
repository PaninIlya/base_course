import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#создание пространства и подпространства для анимации
fig, ax = plt.subplots()
#объект анимации
anim_object, = plt.plot([], [], '-', lw = 2) #запятая создает кортеж(/убирает)

x, y = [], []#Координаты объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)#параметр перебирается от 0 до 2 пи

ax.set_xlim(0, 2*np.pi)#пределы изменения переменной x
ax.set_ylim(-1, 1)#пределы изменения переменной y

#Функция подстановки параметра в объект анимации
def update(frame):
    x.append(frame)
    y.append(np.sin(frame))

    #Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, #Вызов пространства для анимации
                    update,
                     frames = frames_interval, #Интервал значений
                     interval=50)#Интервал между кадрами , по умолчанию 200 милисекунд(в нашем случае 50 милисекунд)


ani.save('animation_1.gif', writer = 'pillow')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0+ R * np.cos(alpha)
    y = y0 + R* np.sin(alpha)
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color = 'r', label = 'Ball')
# ball_line, = plt.plot([], [], '-', color = 'r', label = 'Ball')

frames = 180
coords = np.zeros((frames, 2))

def animate(i):
    # coords[i] = circle_move(R=0.5, vx0 = 2, vy0 = 2, time=i)
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))#текущие значения
    # ball_line.set_data([coords[:i, 0]], [coords[:i, 1]])#все значения до текущего
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('ani3.gif', writer='pillow')
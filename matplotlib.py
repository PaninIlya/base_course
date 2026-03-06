import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def create_sphere_points(radius=1.0, num_points=1000):
    """Создает точки на поверхности сферы"""
    # Генерируем случайные точки на сфере
    phi = np.random.uniform(0, 2 * np.pi, num_points)  # азимутальный угол
    theta = np.arccos(2 * np.random.uniform(0, 1, num_points) - 1)  # полярный угол

    # Преобразуем в декартовы координаты
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)

    return x, y, z


def calculate_lighting(point, light_pos, light_color, sphere_center=(0, 0, 0)):
    """
    Рассчитывает освещение для точки на сфере

    Parameters:
    - point: координаты точки на сфере
    - light_pos: позиция источника света
    - light_color: цвет света (RGB)
    - sphere_center: центр сферы

    Returns:
    - освещенный цвет точки
    """
    # Вектор от центра сферы к точке (нормаль поверхности)
    normal = np.array(point) - np.array(sphere_center)
    normal = normal / np.linalg.norm(normal)

    # Вектор от точки к источнику света
    to_light = np.array(light_pos) - np.array(point)
    to_light = to_light / np.linalg.norm(to_light)

    # Косинус угла между нормалью и направлением на свет
    # (закон Ламберта: яркость пропорциональна cos угла)
    cos_angle = np.dot(normal, to_light)

    # Базовый цвет точки (серый)
    base_color = np.array([0.7, 0.7, 0.7])

    if cos_angle > 0:
        # Точка освещена
        # Интенсивность освещения зависит от угла
        intensity = cos_angle

        # Смешиваем базовый цвет с цветом света
        lit_color = base_color * (1 - intensity * 0.5) + np.array(light_color) * intensity

        # Добавляем небольшую подсветку от окружающего света
        ambient = 0.3
        lit_color = lit_color * (1 - ambient) + base_color * ambient
    else:
        # Точка в тени (только окружающий свет)
        ambient = 0.2
        lit_color = base_color * ambient

    # Ограничиваем значения в пределах [0, 1]
    lit_color = np.clip(lit_color, 0, 1)

    return lit_color


def create_light_rays(light_pos, sphere_points, num_rays=20):
    """
    Создает лучи от источника света к сфере (для визуализации)
    """
    rays_x = []
    rays_y = []
    rays_z = []
    ray_colors = []

    # Выбираем случайные точки на сфере для лучей
    indices = np.random.choice(len(sphere_points[0]), num_rays, replace=False)

    for idx in indices:
        point = [sphere_points[0][idx], sphere_points[1][idx], sphere_points[2][idx]]

        # Добавляем начальную точку луча (источник света)
        rays_x.append(light_pos[0])
        rays_y.append(light_pos[1])
        rays_z.append(light_pos[2])

        # Добавляем конечную точку луча (точка на сфере)
        rays_x.append(point[0])
        rays_y.append(point[1])
        rays_z.append(point[2])

        # Добавляем NaN для разделения лучей
        rays_x.append(np.nan)
        rays_y.append(np.nan)
        rays_z.append(np.nan)

        # Цвет луча соответствует цвету света
        ray_colors.append(light_color)

    return rays_x, rays_y, rays_z, ray_colors


# ================ ОСНОВНАЯ ПРОГРАММА ================

# Параметры
radius = 2.0
num_points = 2000

# Позиция источника света (вне сферы)
light_pos = [4, 2, 3]  # x, y, z
# light_pos = [0, 0, 3]  # можно попробовать и так

# Цвет источника света (RGB)
light_color = [1.0, 0.3, 0.2]  # красноватый

# Создаем точки сферы
x, y, z = create_sphere_points(radius, num_points)

# Рассчитываем цвета для каждой точки
colors = []
for i in range(len(x)):
    point = [x[i], y[i], z[i]]
    color = calculate_lighting(point, light_pos, light_color)
    colors.append(color)

# Создаем лучи для визуализации
ray_x, ray_y, ray_z, ray_colors = create_light_rays(light_pos, (x, y, z), num_rays=30)

# Визуализация
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Рисуем сферу (точки)
scatter = ax.scatter(x, y, z,
                     c=colors,  # цвета точек
                     s=20,  # размер точек
                     alpha=0.9)  # прозрачность

# Рисуем лучи света
for i in range(0, len(ray_x) - 2, 3):
    ax.plot([ray_x[i], ray_x[i + 1]],
            [ray_y[i], ray_y[i + 1]],
            [ray_z[i], ray_z[i + 1]],
            color=light_color, alpha=0.3, linewidth=1)

# Рисуем источник света
ax.scatter(*light_pos,
           c=[light_color],
           s=200,
           marker='*',
           edgecolors='yellow',
           linewidth=2,
           label='Light Source')

# Настройка внешнего вида
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Сфера с освещением\nЦвет источника: RGB{light_color}')

# Добавляем информацию о свете
info_text = f'Источник света: ({light_pos[0]}, {light_pos[1]}, {light_pos[2]})\n'
info_text += f'Цвет: RGB{tuple(light_color)}'
ax.text2D(0.02, 0.98, info_text, transform=ax.transAxes,
          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Настраиваем равные пропорции осей
max_range = radius + max(abs(light_pos[0]), abs(light_pos[1]), abs(light_pos[2]))
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(-max_range, max_range)

plt.tight_layout()
plt.show()


# ================ ДОПОЛНИТЕЛЬНО: АНИМАЦИЯ С ДВИЖУЩИМСЯ СВЕТОМ ================

def animate_light():
    """Анимирует движение источника света вокруг сферы"""
    from matplotlib.animation import FuncAnimation

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Создаем точки сферы (один раз)
    x_sphere, y_sphere, z_sphere = create_sphere_points(radius, 1000)

    scatter = ax.scatter(x_sphere, y_sphere, z_sphere, c='gray', s=10, alpha=0.6)
    light_point = ax.scatter([], [], [], c='red', s=200, marker='*')

    def update(frame):
        # Двигаем источник света по кругу
        angle = frame * 0.1
        light_x = 4 * np.cos(angle)
        light_y = 4 * np.sin(angle)
        light_z = 2 * np.sin(angle * 0.5)  # небольшие колебания по Z

        # Обновляем цвета точек
        colors = []
        for i in range(len(x_sphere)):
            point = [x_sphere[i], y_sphere[i], z_sphere[i]]
            color = calculate_lighting(point, [light_x, light_y, light_z], light_color)
            colors.append(color)

        scatter.set_color(colors)
        light_point._offsets3d = ([light_x], [light_y], [light_z])

        return scatter, light_point

    ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)
    plt.show()
    return ani

# Раскомментируйте для анимации:
# animate_light()
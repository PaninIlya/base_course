import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 1, 100)
n_points = 2000
phi = np.random.uniform(0, 2 * np.pi, n_points)
theta = np.random.uniform(0, np.pi, n_points)
R = 6
# RGB для желтого цвета света
light_color = [1.0, 0.9, 0.3]

x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)

start_x, start_y, start_z = R + 1, R + 1, R + 1

n_light_points = 200
phi_light = np.random.uniform(0, 2 * np.pi, n_light_points)
theta_light = np.random.uniform(0, np.pi, n_light_points)

n_random_rays = 65
phi_random = np.random.uniform(0, 2 * np.pi, n_random_rays)
theta_random = np.random.uniform(0, np.pi, n_random_rays)


def spinnig_func(frame):
    ax.clear()

    rotation_speed = frame * 0.025

    x_rotation = x * np.cos(rotation_speed) - y * np.sin(rotation_speed)
    y_rotation = x * np.sin(rotation_speed) + y * np.cos(rotation_speed)
    z_rotation = z

    # Создаем массив для накопления интенсивности от всех источников
    total_intensity = np.zeros(len(x))

    # 1. Сначала учитываем вклад основного источника света
    for i in range(len(x)):
        point = [x_rotation[i], y_rotation[i], z_rotation[i]]
        normal_vector = np.array(point) - np.array([0, 0, 0])
        normal_vector = normal_vector / np.linalg.norm(normal_vector)

        vector_to_light = np.array([start_x, start_y, start_z]) - np.array(point)
        vector_to_light = vector_to_light / np.linalg.norm(vector_to_light)

        cos_angle = np.dot(normal_vector, vector_to_light)

        if cos_angle > 0:
            total_intensity[i] += cos_angle * 0.8  # основной источник

    # 2. Учитываем вклад случайных лучей, которые попадают на сферу
    for j in range(n_random_rays):
        direction_x = np.sin(theta_random[j]) * np.cos(phi_random[j])
        direction_y = np.sin(theta_random[j]) * np.sin(phi_random[j])
        direction_z = np.cos(theta_random[j])

        # Находим пересечение со сферой
        a_ray = direction_x ** 2 + direction_y ** 2 + direction_z ** 2
        b_ray = 2 * (start_x * direction_x + start_y * direction_y + start_z * direction_z)
        c_ray = (start_x ** 2 + start_y ** 2 + start_z ** 2) - R ** 2

        discriminant = b_ray ** 2 - 4 * a_ray * c_ray

        if discriminant > 0:
            t1 = (-b_ray + np.sqrt(discriminant)) / (2 * a_ray)
            t2 = (-b_ray - np.sqrt(discriminant)) / (2 * a_ray)

            ray_crossing = None
            if t1 > 10 ** (-6):
                ray_crossing = t1
            if t2 > 10 ** (-6) and (ray_crossing is None or t2 < ray_crossing):
                ray_crossing = t2

            if ray_crossing is not None:
                # Точка попадания луча на сферу
                hit_x = start_x + ray_crossing * direction_x
                hit_y = start_y + ray_crossing * direction_y
                hit_z = start_z + ray_crossing * direction_z

                # Находим ближайшую точку на сфере к точке попадания
                distances = np.sqrt((x_rotation - hit_x) ** 2 + (y_rotation - hit_y) ** 2 + (z_rotation - hit_z) ** 2)
                closest_point_idx = np.argmin(distances)

                # Добавляем интенсивность от случайного луча к ближайшей точке
                if distances[closest_point_idx] < 1.0:  # Порог расстояния
                    # Интенсивность зависит от угла падения
                    point = [x_rotation[closest_point_idx], y_rotation[closest_point_idx],
                             z_rotation[closest_point_idx]]
                    normal_vector = np.array(point) - np.array([0, 0, 0])
                    normal_vector = normal_vector / np.linalg.norm(normal_vector)

                    vector_to_random = np.array([start_x, start_y, start_z]) - np.array(point)
                    vector_to_random = vector_to_random / np.linalg.norm(vector_to_random)

                    cos_angle_random = np.dot(normal_vector, vector_to_random)

                    if cos_angle_random > 0:
                        total_intensity[
                            closest_point_idx] += cos_angle_random * 0.5  # случайный источник с меньшей интенсивностью

    # Создаем цвета для точек сферы на основе накопленной интенсивности
    colors_sphere = []
    base_point_color = np.array([0.5, 0.5, 0.5])

    for i in range(len(x)):
        intensity = total_intensity[i]
        intensity = np.clip(intensity, 0, 1)  # Ограничиваем интенсивность

        if intensity > 0:
            point_color = base_point_color * (1 - intensity * 0.7) + np.array(light_color) * intensity
            koef = 0.2
            point_color = point_color * (1 - koef) + base_point_color * koef
            point_color = np.clip(point_color, 0, 1)
        else:
            koef2 = 0.15
            point_color = base_point_color * koef2
            point_color = np.clip(point_color, 0, 1)

        colors_sphere.append(point_color)

    # рисуем сферу
    scatter = ax.scatter(x_rotation, y_rotation, z_rotation, c=colors_sphere, s=45, alpha=0.7)

    # Рисуем случайные лучи
    for i in range(n_random_rays):
        direction_x = np.sin(theta_random[i]) * np.cos(phi_random[i])
        direction_y = np.sin(theta_random[i]) * np.sin(phi_random[i])
        direction_z = np.cos(theta_random[i])

        # Находим пересечение со сферой
        a_ray = direction_x ** 2 + direction_y ** 2 + direction_z ** 2
        b_ray = 2 * (start_x * direction_x + start_y * direction_y + start_z * direction_z)
        c_ray = (start_x ** 2 + start_y ** 2 + start_z ** 2) - R ** 2

        discriminant = b_ray ** 2 - 4 * a_ray * c_ray

        if discriminant > 0:
            t1 = (-b_ray + np.sqrt(discriminant)) / (2 * a_ray)
            t2 = (-b_ray - np.sqrt(discriminant)) / (2 * a_ray)

            ray_crossing = None
            if t1 > 10 ** (-6):
                ray_crossing = t1
            if t2 > 10 ** (-6) and (ray_crossing is None or t2 < ray_crossing):
                ray_crossing = t2

            if ray_crossing is not None:
                # Луч попадает на сферу - рисуем желтым
                t_ray = np.linspace(0, 1, 50)
                target_x = start_x + ray_crossing * direction_x
                target_y = start_y + ray_crossing * direction_y
                target_z = start_z + ray_crossing * direction_z

                ray_x = start_x + (target_x - start_x) * t_ray
                ray_y = start_y + (target_y - start_y) * t_ray
                ray_z = start_z + (target_z - start_z) * t_ray

                ax.plot(ray_x, ray_y, ray_z, color='yellow', linewidth=1, alpha=0.5)
            else:

                ray_x = start_x + direction_x * t * R ** 2
                ray_y = start_y + direction_y * t * R ** 2
                ray_z = start_z + direction_z * t * R ** 2

                ax.plot(ray_x, ray_y, ray_z, color='yellow', linewidth=0.5, alpha=0.3)
        else:

            ray_x = start_x + direction_x * t * R ** 2
            ray_y = start_y + direction_y * t * R ** 2
            ray_z = start_z + direction_z * t * R ** 2

            ax.plot(ray_x, ray_y, ray_z, color='yellow', linewidth=0.5, alpha=0.3)

    # Рисуем лучи от основного источника к сфере
    for i in range(n_light_points):
        vector_x = np.sin(theta_light[i]) * np.cos(phi_light[i])
        vector_y = np.sin(theta_light[i]) * np.sin(phi_light[i])
        vector_z = np.cos(theta_light[i])

        a = vector_x ** 2 + vector_y ** 2 + vector_z ** 2
        b = 2 * (start_x * vector_x + start_y * vector_y + start_z * vector_z)
        c = (start_x ** 2 + start_y ** 2 + start_z ** 2) - R ** 2

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            t1 = (-b + np.sqrt(discriminant)) / (2 * a)
            t2 = (-b - np.sqrt(discriminant)) / (2 * a)

            light_crossing = None
            if t1 > 10 ** (-6):
                light_crossing = t1
            if t2 > 10 ** (-6) and (light_crossing is None or t2 < light_crossing):
                light_crossing = t2

            if light_crossing is not None:
                t_light = np.linspace(0, 1, 50)
                target_x = start_x + light_crossing * vector_x
                target_y = start_y + light_crossing * vector_y
                target_z = start_z + light_crossing * vector_z

                light_x = start_x + (target_x - start_x) * t_light
                light_y = start_y + (target_y - start_y) * t_light
                light_z = start_z + (target_z - start_z) * t_light

                alpha = np.random.uniform(0.1, 0.3)
                ax.plot(light_x, light_y, light_z, color=light_color, linewidth=0.8, alpha=alpha)

    # это источник света
    ax.scatter([start_x], [start_y], [start_z], c='yellow', s=200, marker='o', edgecolors='orange')

    ax.set_xlabel('X координата')
    ax.set_ylabel('Y координата')
    ax.set_zlabel('Z координата')
    ax.set_title('Photometry')

    ax.set_xlim([-R - 2, R + 2])
    ax.set_ylim([-R - 2, R + 2])
    ax.set_zlim([-R - 2, R + 2])

    return ax,


# Создаем анимацию
anim = FuncAnimation(fig, spinnig_func, frames=200, interval=50, blit=False)
plt.show()
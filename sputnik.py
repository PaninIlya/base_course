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

n_points_small = 300
phi_small = np.random.uniform(0, 2 * np.pi, n_points_small)
theta_small = np.random.uniform(0, np.pi, n_points_small)

R = 6
R_small = 1.5
light_color = [1.0, 0.9, 0.3]

x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)

# Позиция источника света
start_x, start_y, start_z = R + 2, R + 2, R + 2

# Направление от центра большой сферы к источнику света
direction_to_light = np.array([start_x, start_y, start_z]) - np.array([0, 0, 0])
direction_to_light = direction_to_light / np.linalg.norm(direction_to_light)

# Позиция маленькой сферы (на линии между источником и большой)
distance_from_center = R + R_small + 1.5
small_x = direction_to_light[0] * distance_from_center
small_y = direction_to_light[1] * distance_from_center
small_z = direction_to_light[2] * distance_from_center

x_small_unit = R_small * np.sin(theta_small) * np.cos(phi_small)
y_small_unit = R_small * np.sin(theta_small) * np.sin(phi_small)
z_small_unit = R_small * np.cos(theta_small)

x_small = x_small_unit + small_x
y_small = y_small_unit + small_y
z_small = z_small_unit + small_z

n_light_points = 200
phi_light = np.random.uniform(0, 2 * np.pi, n_light_points)
theta_light = np.random.uniform(0, np.pi, n_light_points)

n_random_rays = 30
phi_random = np.random.uniform(0, 2 * np.pi, n_random_rays)
theta_random = np.random.uniform(0, np.pi, n_random_rays)


def spinnig_func(frame):
    ax.clear()
    ax.set_facecolor('black')

    rotation_speed = frame * 0.025
    rotation_speed_small = frame * 0.1

    x_rotation = x * np.cos(rotation_speed) - y * np.sin(rotation_speed)
    y_rotation = x * np.sin(rotation_speed) + y * np.cos(rotation_speed)
    z_rotation = z

    x_rotation_small = x_small_unit * np.cos(rotation_speed_small) - y_small_unit * np.sin(
        rotation_speed_small) + small_x
    y_rotation_small = x_small_unit * np.sin(rotation_speed_small) + y_small_unit * np.cos(
        rotation_speed_small) + small_y
    z_rotation_small = z_small_unit + small_z

    colors_sphere_big = []

    for i in range(len(x)):
        point = np.array([x_rotation[i], y_rotation[i], z_rotation[i]])
        normal_vector = point / np.linalg.norm(point)

        # Вектор от точки к источнику света
        to_light = np.array([start_x, start_y, start_z]) - point
        to_light = to_light / (np.linalg.norm(to_light) + 1e-10)

        # Косинус угла между нормалью и направлением на свет
        cos_angle = np.dot(normal_vector, to_light)

        # Базовая интенсивность (только освещенная сторона)
        if cos_angle > 0:
            intensity = cos_angle
        else:
            intensity = 0

        # ============ ПРОВЕРКА ТЕНИ ============
        # Вектор от источника к точке
        light_to_point = point - np.array([start_x, start_y, start_z])
        distance_to_point = np.linalg.norm(light_to_point)

        if distance_to_point > 1e-6:
            light_to_point = light_to_point / distance_to_point

        # Вектор от источника к центру маленькой сферы
        to_small_center = np.array([small_x, small_y, small_z]) - np.array([start_x, start_y, start_z])

        # Находим ближайшую точку на луче к центру маленькой сферы
        t_proj = np.dot(to_small_center, light_to_point)

        in_shadow = False

        if t_proj > 0:  # Маленькая сфера впереди по направлению луча
            # Точка на луче, ближайшая к центру маленькой сферы
            closest_point = np.array([start_x, start_y, start_z]) + light_to_point * t_proj
            dist_to_center = np.linalg.norm(closest_point - np.array([small_x, small_y, small_z]))

            # Если расстояние меньше радиуса, луч пересекает сферу
            if dist_to_center < R_small:
                # Расстояние от источника до точки пересечения
                half_chord = np.sqrt(R_small ** 2 - dist_to_center ** 2)
                t_hit = t_proj - half_chord

                # Если пересечение происходит до точки на большой сфере
                if t_hit > 1e-6 and t_hit < distance_to_point:
                    in_shadow = True

        # Применяем цвет
        if intensity > 0 and not in_shadow:
            # Освещенная область
            point_color = np.array([0.5, 0.5, 0.5]) * (0.3 + intensity * 0.7)
            point_color += np.array(light_color) * intensity * 0.6
            point_color = np.clip(point_color, 0, 1)
        elif in_shadow:
            # Область тени (темная, но не черная)
            point_color = np.array([0.08, 0.08, 0.12])
        else:
            # Ночная сторона (очень темная)
            point_color = np.array([0.03, 0.03, 0.05])

        colors_sphere_big.append(point_color)

    ax.scatter(x_rotation, y_rotation, z_rotation, c=colors_sphere_big, s=45, alpha=0.8)

    # Маленькая сфера
    colors_sphere_small = []
    for i in range(len(x_small_unit)):
        point = np.array([x_rotation_small[i], y_rotation_small[i], z_rotation_small[i]])
        normal_vector = point - np.array([small_x, small_y, small_z])
        normal_vector = normal_vector / (np.linalg.norm(normal_vector) + 1e-10)

        to_light = np.array([start_x, start_y, start_z]) - point
        to_light = to_light / (np.linalg.norm(to_light) + 1e-10)

        cos_angle = np.dot(normal_vector, to_light)

        if cos_angle > 0:
            intensity = cos_angle
            point_color = np.array([0.6, 0.4, 0.3]) * (0.3 + intensity * 0.7)
            point_color += np.array(light_color) * intensity * 0.5
            point_color = np.clip(point_color, 0, 1)
        else:
            point_color = np.array([0.15, 0.1, 0.08])

        colors_sphere_small.append(point_color)

    ax.scatter(x_rotation_small, y_rotation_small, z_rotation_small, c=colors_sphere_small, s=35, alpha=0.9)

    # Случайные лучи (как в изначальном коде)
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
                t_ray = np.linspace(0, 1, 50)
                target_x = start_x + ray_crossing * direction_x
                target_y = start_y + ray_crossing * direction_y
                target_z = start_z + ray_crossing * direction_z

                ray_x = start_x + (target_x - start_x) * t_ray
                ray_y = start_y + (target_y - start_y) * t_ray
                ray_z = start_z + (target_z - start_z) * t_ray

                ax.plot(ray_x, ray_y, ray_z, color='yellow', linewidth=1, alpha=0.5)

    # Лучи от источника света
    for i in range(n_light_points):
        # векторы, куда будет падать луч (относительно центра сферы)
        vector_x = np.sin(theta_light[i]) * np.cos(phi_light[i])
        vector_y = np.sin(theta_light[i]) * np.sin(phi_light[i])
        vector_z = np.cos(theta_light[i])

        # нахождение точек пересечения (ур-е решается относительно t)
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

                # сами лучи
                light_x = start_x + (target_x - start_x) * t_light
                light_y = start_y + (target_y - start_y) * t_light
                light_z = start_z + (target_z - start_z) * t_light

                alpha = np.random.uniform(0.1, 0.3)
                ax.plot(light_x, light_y, light_z, color=light_color, linewidth=0.8, alpha=alpha)

    # это источник света
    ax.scatter([start_x], [start_y], [start_z], c='yellow', s=200, marker='o', edgecolors='orange')

    ax.set_xlabel('X coord', color='white')
    ax.set_ylabel('Y coord', color='white')
    ax.set_zlabel('Z coord', color='white')

    ax.tick_params(axis='x', colors='white', labelsize=9)
    ax.tick_params(axis='y', colors='white', labelsize=9)
    ax.tick_params(axis='z', colors='white', labelsize=9)
    ax.set_title('Photometry - Тень от маленькой планеты', color='white')

    ax.set_xlim([-R - 2, max(start_x, small_x) + 2])
    ax.set_ylim([-R - 2, max(start_y, small_y) + 2])
    ax.set_zlim([-R - 2, max(start_z, small_z) + 2])

    return ax,


anim = FuncAnimation(fig, spinnig_func, frames=200, interval=50, blit=False)

plt.show()
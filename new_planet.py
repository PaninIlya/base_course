import pyvista as pv
import numpy as np
import random
R = float(input('Введите радиус планеты: '))
sphere = pv.Sphere(radius=R, phi_resolution=100, theta_resolution=100)


N = int(input('Введите количество кратеров(0 - 25): '))








for i in range(N):
    try:
        random_vertex_index = random.randint(0, sphere.n_points - 1)
        random_point = sphere.points[random_vertex_index]


        crater_sphere = pv.Sphere(radius=0.4*R, center=(random_point[0]*1.3, random_point[1]*1.3, random_point[2]*1.3))


        sphere = sphere.boolean_difference(crater_sphere)


    except ValueError:
        break

for i in range(len(sphere.points) // 2):
    random_vertex_index = random.randint(0, sphere.n_points - 1)
    random_point = sphere.points[random_vertex_index]
    random_point *= 1.01

plotter = pv.Plotter()

plotter.add_mesh(sphere, color = 'grey', show_edges = True)

plotter.show()
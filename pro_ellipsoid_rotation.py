import pyvista as pv
import numpy as np
import time


sphere = pv.Sphere(radius=1.0, theta_resolution=50, phi_resolution=50, center=(0,3,0))
planet = pv.Sphere(radius=2)

points = sphere.points
points[:, 0] = points[:, 0] * 2.0  #Растягиваем по X(берем весь("0") первый столбец(первый столбец - X координата) срезом(':') )
points[:, 1] = points[:, 1] * 1.5  #Растягиваем по Y
points[:, 2] = points[:, 2] * 0.8  #Сжимаем по Z
sphere.points = points


pl = pv.Plotter(lighting=None)

sphere_rotate = pl.add_mesh(sphere, color='orange', specular=0.7, smooth_shading=True, show_edges=True)
pl.show_axes()

# grid = pv.Plane(i_size=4, j_size=4)#добавление платформы,чтобы за наблюдать за распространением света
# pl.add_mesh(grid, ambient=0, diffuse=0.5, specular=0.8, color='white')
planet_rotate = pl.add_mesh(planet, color='blue', specular=0.7, smooth_shading=True, show_edges=True)


light = pv.Light(
    position=(0, 0, 10), show_actor=True, positional=True,
    cone_angle=30, exponent=20, intensity=2

)


pl.camera_position = 'iso'
# pl.enable_shadows()
pl.set_background('darkgrey')
pl.add_light(light)

pl.show(interactive_update=True)



while True:
        sphere_rotate.rotate_x(2)
        planet_rotate.rotate_z(1)
        pl.update()
        time.sleep(0.05)



import pyvista as pv
import numpy as np
import time

sphere_radius = int(input(f'Введите радиус спутника: '))
planet_radius = int(input(f'Введите радиус планеты:  '))

sphere_color = input(f'Введите цвет спутника(Пр: "orange", "darkgrey" ): ')
planter_color = input(f'Введите цвет планеты(Пр: "orange", "darkgrey"): ')

sphere = pv.Sphere(radius=sphere_radius, theta_resolution=50, phi_resolution=50, center=(0,sphere_radius+planet_radius+1,0))
planet = pv.Sphere(radius=planet_radius)

intensity_selection = int(input(f'Введите интенсивность света(не рекомендуется больше 5(кроме случаев с темными цветами поверхностей)): '))
exponent_selection = int(input(f'Введите экспоненту (насколько свет сконцентрирорван и резок; рекомендуется до 40): '))
cone_angle_selection = int(input(f'Введите угол падения света (конусообразный; не рекомендуется больше 90): '))

points = sphere.points
points[:, 0] = points[:, 0] * 2.0  #Растягиваем по X(берем весь("0") первый столбец(первый столбец - X координата) срезом(':') )
points[:, 1] = points[:, 1] * 1.5  #Растягиваем по Y
points[:, 2] = points[:, 2] * 0.8  #Сжимаем по Z
sphere.points = points


pl = pv.Plotter(lighting=None)

sphere_rotate = pl.add_mesh(sphere, color=sphere_color, specular=0.9, smooth_shading=True, show_edges=True)
pl.show_axes()

# grid = pv.Plane(i_size=4, j_size=4)#добавление платформы,чтобы за наблюдать за распространением света
# pl.add_mesh(grid, ambient=0, diffuse=0.5, specular=0.8, color='white')
planet_rotate = pl.add_mesh(planet, color=planter_color, specular=0.9, smooth_shading=True, show_edges=True)

z_coord_light = (sphere_radius + planet_radius)*4
x_coord_light = (sphere_radius + planet_radius)
light = pv.Light(
    position=(0, 0, z_coord_light), show_actor=True, positional=True,
    cone_angle=cone_angle_selection, exponent=exponent_selection, intensity=intensity_selection

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



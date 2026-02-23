import pyvista as pv
import numpy as np
import time


sphere = pv.Sphere(radius=1.0, theta_resolution=50, phi_resolution=50)
points = sphere.points
points[:, 0] = points[:, 0] * 2.0  #Растягиваем по X
points[:, 1] = points[:, 1] * 1.5  #Растягиваем по Y
points[:, 2] = points[:, 2] * 0.8  #Сжимаем по Z
sphere.points = points


pl = pv.Plotter()

light = pv.Light(
    position=(99, 0, 6),
    cone_angle=30,
    intensity=2,
    color='white'
)


sphere_rotate = pl.add_mesh(sphere, color='orange', specular=0.7, smooth_shading=True, show_edges=True)
pl.show_axes()
pl.camera_position = 'iso'
pl.add_light(light)

pl.show(interactive_update=True) 



while True:
        sphere_rotate.rotate_z(2)  
        pl.update()  
        time.sleep(0.05)  



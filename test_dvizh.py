import pyvista as pv
import numpy as np


sphere = pv.Sphere(radius=0.3, center=(0, 0, 0))
plotter = pv.Plotter()

follow_light = pv.Light(
    position=(0, 0, 2),
    focal_point=sphere.center,
    color='yellow',
    intensity=0.8,
    positional=True,
    cone_angle=45
)

plotter.add_mesh(sphere, color='red')
plotter.add_light(follow_light)


def update_position(step):
    x = np.sin(step * 0.1) * 2
    y = np.cos(step * 0.1) * 2
    z = np.sin(step * 0.2) * 0.5
    

    sphere.translate([x - sphere.center[0], 
                      y - sphere.center[1], 
                      z - sphere.center[2]], inplace=True)
    

    follow_light.position = (x, y, z + 2)  #свет над сферой
    follow_light.focal_point = (x, y, z)   #направлен на сферу
    
    # Обновляем меш в сцене
    plotter.add_mesh(sphere, color='red', name='moving_sphere')
    return sphere

plotter.show()
for i in range(100):
    update_position(i)
    plotter.render()
    plotter.update()
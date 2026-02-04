import pyvista as pv

plotter = pv.Plotter(lighting='three lights')  #предустановки освещения
mesh = pv.Quadrilateral()#создание квадрата
#добавление объекта с настройками материала
plotter.add_mesh(
    mesh,
    color='lightblue',
    pbr=True,  # Physically Based Rendering
    metallic=0.8,  #металличность (0-1)
    roughness=0.2,  #шероховатость (0-1)
    smooth_shading=True
)

plotter.show()
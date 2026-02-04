import pyvista as pv
plotter = pv.Plotter()

#добавление пользовательских источников света
light1 = pv.Light(
    position=(1, 1, 1),  #позиция в  координатах
    focal_point=(0, 0, 0),  #точка, куда напрвлен свет
    color='white',
    intensity=0.8, #интенсивность
    positional=True,  #точечный источник (False - направленный(как обычный свет), True - просто луч(при малых углах))
    cone_angle=30,    #угол конуса (для позиционных)
    exponent=2        #затухание(регулировка площади света )
)

light2 = pv.Light( #можно создавать несколько пользовательских источников
    position=(-1, -1, 1),
    color='blue',
    intensity=0.3
)

plotter.add_light(light1)#добавление пользовательского света
plotter.add_light(light2)
plotter.add_mesh(pv.Sphere())#добавляем объект в сетку координат
plotter.show()
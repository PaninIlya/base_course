import pyvista as pv

mesh = pv.Sphere()
mesh.plot(
    lighting=True,  # включить освещение (по умолчанию True)
    smooth_shading=True,  # сглаживание нормалей
    show_edges=True,
    color='white',
    specular=0.5,    # интенсивность бликов (зеркальности)
    specular_power=50,  # размер/резкость бликов
    diffuse=0.5,     # интенсивность рассеянного света
    ambient=0.3      # интенсивность фонового света
)
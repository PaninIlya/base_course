def solar_sys_generator():
    #Создаем итератор при помощи генератора
    for i in ['mercury', 'venus', 'earth']:
        yield i

planets = solar_sys_generator()
iter_planets = iter(planets)
print(type(planets))
print(next(planets))
print(next(planets))
print(next(planets))
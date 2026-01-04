class Planet:
    @staticmethod#описывает сам класс, а не его объекты
    def is_big_planet(diameter):
        if diameter > 10000:
            return True
        else:
            return False


Planet.is_big_planet(100)
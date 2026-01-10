class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name

    def __getitem__(self, key):
        return print(self.planets[key])
    
system1 = StarSystem(['pl1', 'pl2'], 'Systwm1')
system1[0]
system1[1]
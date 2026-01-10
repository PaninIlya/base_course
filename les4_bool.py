class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
    
    def __bool__(self):
        return len(self.planets) > 0
    
system1 = StarSystem(['pl1', 'pl2'], 'System1')
system2 = StarSystem([], 'System2')

print(bool(system1))
print(bool(system2))
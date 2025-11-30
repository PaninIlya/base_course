from Army import Army

army = {'Human': 0, 'Giant': 0, 'Canon': 0}

class Castle:
    def __init__(self, color):
        self.hp = 0     
        self.dmg = 0  
        self.color = color
        self.army = {'Human': 0, 'Giant': 0, 'Canon': 0}


    def army_creation(self, type, kol):
        self.type = type
        self.kol = kol
        self.army[self.type] += self.kol
        print(self.army)
        self.dmg += Army(self.type).dmg * self.kol
        self.hp += Army(self.type).hp * self.kol
        print(self.dmg, self.hp)


    
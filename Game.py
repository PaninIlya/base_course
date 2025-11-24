color_selector = {1: 'Red', 2: 'Green', 3: 'Blue'}


class Castle:
    def __init__(self, index):
        self.index = index
        self.hp = 10000
        self.army = []
        self.player_money = 10000

class Warrior:
    def __init__(self, index, war):
        self.index = index
        self.war = war
        if self.war == 'Human':
            self.hp = 100
            self.dmg = 50
            self.price = 75
        elif self.war == 'Giant':
            self.hp = 1000
            self.dmg = 250
            self.price = 400
        elif self.war == 'Archer':
            self.hp = 75
            self.dmg = 100
            self.price = 125        
        

class Player:
    def __init__(self, color):
        self.color = color

    
    def buy_army(self):
        if 

color = Player(int(input(f'Выберите цвет игрока {color_selector} \n')))
castle = Castle(color)
warrior = Warrior(color, )
class Army:
    def __init__ (self, color, type, hp, dmg, price):
        self.type = type
        self.color = color
        # if self.type == 'Human':
        #     self.hp = 50
        #     self.dmg = 50
        #     self.price = 20
        # elif self.type == 'Giant':
        #     self.hp = 500
        #     self.dmg = 300
        #     self.price = 350
        # elif self.type == 'Canon':
        #     self.hp = 200
        #     self.dmg = 500
        #     self.price = 450
        self.hp = hp
        self.dmg = dmg
        self.price = price
    

    def __str__(self):
        return self.type

Human = Army('red', 'Human', 50, 50, 20) 
Giant = Army('red','Giant', 500, 300, 350)
Canon = Army("red",'Canon', 200, 500, 450)       
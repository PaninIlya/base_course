class Army:
    def __init__(self, type):
        self.type = type
        if self.type == 'Human':
            self.hp = 50
            self.dmg = 50
            self.price = 20
        elif self.type == 'Giant':
            self.hp = 500
            self.dmg = 300
            self.price = 350
        elif self.type == 'Canon':
            self.hp = 200
            self.dmg = 500
            self.price = 450
        
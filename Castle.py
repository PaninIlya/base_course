from Army import Army, Human, Giant, Canon

army = {'Human': 0, 'Giant': 0, 'Canon': 0}

def stats():
    print(f'''
                        ===================================
                       │ Начальное здоровье вашего замка:  │
                       │              50000                │
                       │Уровень его защиты(урон армии):    │
                       │                0                  │
                        ===================================
          
          ''')
class Castle:
    def __init__(self, color):
        self.hp = 50000     
        self.dmg = 0
        self.money = 4500000  
        self.color = color
        self.army = {'Human': 0, 'Giant': 0, 'Canon': 0}


    def army_creation(self, unit_type, kol):
        self.unit_type = unit_type
        self.kol = kol
        self.army_hp = 0
        self.army_dmg = 0

        if self.money >= unit_type.price * self.kol:
            self.army_hp += unit_type.hp * self.kol
            # print(self.army)
            self.money -= unit_type.price * self.kol
            self.dmg += unit_type.dmg * self.kol
            self.hp += unit_type.hp * self.kol
            self.army[unit_type.type] += self.kol
            print(f'''
                        =====================================
                       │  Урон армии игрока {self.color}: {self.dmg}     │
                       │  Здоровье армии игрока {self.color}: {self.army_hp} │
                        =====================================
              
              ''')
            print(f'Армия игрока {self.color}: {self.army}')
            print(f"У игрока {self.color} осталось {self.money} денег")
        else:
            self.money = 0
            print('У вас нет денег')

    def __str__(self):
        return self.color

# red = Castle('red')
# green = Castle('green')

stat = stats()
print(stat)


# red.army_creation(Human, 10)
# green.army_creation(Canon, 10)



    
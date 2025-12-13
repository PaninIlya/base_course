from Army import Army
from Army import Human, Giant, Canon
from Castle import Castle, red



class Player:
    def __init__(self, color):
        self.color = color

        


    # def buy_army(self, type, kol):
    #     self.kol = kol
    #     self.type = type
    #     if self.money > Army(self.type).price * self.kol:
    #         self.money -= Army(self.type).price * self.kol
    #         Castle(self.color).army[self.type] += self.kol

    #         Castle(self.color).dmg += Army(self.type).dmg * self.kol 
    #         Castle(self.color).hp += Army(self.type).hp * self.kol 
    #         print(self.money)
    #         print(f'''
    #             ==========================================
    #                    │  Урон армии: {Castle(self.color).dmg}    │
    #                    │  Здоровье армии: {Castle(self.color).hp} │
    #             ==========================================        
              
    #           ''')
            
    #     if self.money < Army(self.type).price * self.kol:
    #         print(f'У вас нет деняк на {Army(self.type)}')

    
pl1 = Player('red')
# pl1.buy_army('Human', 1000)




from NPC import NPC 
from NPC import skeleton, dragon, goblin
from Army import Army
from Castle import *

def start_hero_stats():
     print(f'''
            
            ХП: 10000
            Урон: 1500

        ''')
class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 10000
        self.dmg = 1500
        self.army = {'Human': 0, 'Giant': 0, 'Canon': 0}
        self.army_dmg = 0
        self.army_hp = 0
    

    def attack_npc(self , npc,  kol, current_castle,):
        self.npc = npc
        self.current_castle = current_castle
        self.kol = kol
        if self.hp >  npc.dmg*self.kol and self.dmg > npc.hp*self.kol:
            npc.hp = 0
            self.hp -= npc.dmg*self.kol
            current_castle.money += npc.price * self.kol
            print(f'Ваш герой убил {self.kol} {npc}(ов)')
            print(f"Ваше кол-во денег : {current_castle.money}")
        else:
            self.hp = 0
            print(f'Ваш герой умер, {self.kol} {self.npc} оказались слишком сильны')


    def army_attack_npc(self, npc,  kol,current_castle):
        self.npc = npc

        self.kol = kol
        self.current_castle = current_castle
        hp = current_castle.hp + self.hp
        
        if hp > npc.dmg * self.kol:
            print(f'Ваше общее здоровье: {self.hp}')
            hp -= npc.dmg * self.kol
            current_castle.money += npc.price * self.kol
            print(f"Вы убили {npc}")
            print(f'Ваши деньги: {current_castle.money}')

        else:
            print(f'Ваша армия слишком слаба для атаки {self.kol} {self.npc}')

    def army_attack_player(self, castle1, castle2):

            while castle1.hp > 0 or castle2.hp > 0:

                
                    castle1.hp -= castle2.dmg  
                    castle2.hp -= castle1.dmg 
                    print(f"у армии замка {castle1} осталось { max(castle1.hp,0)} здоровья")
                    print (f"у армии замка {castle2} осталось {max(castle2.hp,0)} здоровья")
            
                    if castle1.hp <= 0:
                        print(f'''
                            =============================== 
                              Победила армия замка {castle2}
                            ===============================


                            ================================ 
                                Игрок {castle1} проиграл
                            ===============================

                             ''')
                        castle2.money += castle1.money
                        castle1.money = 0
                        castle1.hp = 0
                        print(f"у армии замка {castle1} осталось {castle1.hp} здоровья")
                        print(f'У игрока {castle2} теперь столько денег: {castle2.money}')
                        print(f'У игрока {castle1} теперь столько денег: {castle1.money}')
                        
                        break
                    elif castle2.hp <= 0:
                        print(f'''
                             ============================== 
                              Победила армия игрока {castle1}
                             ==============================

                             
                            =============================== 
                                Игрок {castle2} проиграл
                            ===============================

                            ''')
                        castle1.money += castle2.money
                        castle2.money = 0
                        castle2.hp = 0
                        print (f"у армии замка {castle2} осталось {castle2.hp} здоровья")
                        print(f'У игрока {castle2} теперь  {castle2.money} денег')
                        print(f'У игрока {castle1} теперь  {castle1.money} денег')
                    
                        break
    def upgrade_your_hero(self,  current_castle):
        
        self.current_castle = current_castle
        if self.current_castle.money > 100000:
            self.hp += 5000
            self.dmg += 2000
            self.current_castle.money -= 100000
            print(f'''
                  =========================================
                  Теперь хп героя {self.color}: {self.hp}|  урон: {self.dmg}
                  =========================================
                ''')
            print(f'У вас осталось {self.current_castle.money} денег ')
        else:
            print(f'Вам не хватает {100000-self.current_castle.money} для прокачки героя')
        
    # def revive_your_hero(self):
    #     self.hp = 10000
    #     self.dmg = 1500
    #     print(f'Ваш герой был оживлен , его хп : 10000, а урон : 1500')   


# hero = Hero('lol')
# hero.attack_npc(skeleton, 20, red)

# # castle1 = Hero('castle1')
# # castle2 = Hero("castle2")
# hero.army_attack_player(red, green)

# red.army_creation("Human", 150)
# hero.army_attack_npc('Dragon',20 , red, skeleton)
# hero = Hero('adad')
# hero.attack_npc(dragon, 80800, red)
# hero.upgrade_your_hero(red)
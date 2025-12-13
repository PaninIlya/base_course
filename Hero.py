from NPC import NPC 
from NPC import skeleton, dragon, goblin
from Army import Army
from Castle import *


class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 10000
        self.dmg =1500
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
            print(f'Castle {self.hp}')
            hp -= npc.dmg * self.kol
            current_castle.money += npc.price * self.kol
            print(f"Вы убили {npc}")
            print(f'Ваши деньги: {current_castle.money}')

        else:
            print(f'Ваша армия слишком слаба для атаки {self.kol} {self.npc}')

    def army_attack_player(self, hero1, hero2):

            while hero1.hp > 0 or hero2.hp > 0:

                
                    hero1.hp -= hero2.dmg  
                    hero2.hp -= hero1.dmg 
                    print(f"у армии замка {hero1} осталось { max(hero1.hp,0)} здоровья")
                    print (f"у армии замка {hero2} осталось {max(hero2.hp,0)} здоровья")
            
                    if hero1.hp <= 0:
                        print(f'''
                            =============================== 
                              Победила армия замка {hero2}
                            ===============================


                            ================================ 
                                Игрок {hero1} проиграл
                            ===============================

                             ''')
                        hero2.money += hero1.money
                        hero1.money = 0
                        hero1.hp = 0
                        print(f"у армии замка {hero1} осталось {hero1.hp} здоровья")
                        print(f'У игрока {hero2} теперь столько денег: {hero2.money}')
                        print(f'У игрока {hero1} теперь столько денег: {hero1.money}')
                        
                        break
                    elif hero2.hp <= 0:
                        print(f'''
                             ============================== 
                              Победила армия игрока {hero1}
                             ==============================

                             
                            =============================== 
                                Игрок {hero2} проиграл
                            ===============================

                            ''')
                        hero1.money += hero2.money
                        hero2.money = 0
                        hero2.hp = 0
                        print (f"у армии замка {hero2} осталось {hero2.hp} здоровья")
                        print(f'У игрока {hero2} теперь столько денег: {hero2.money}')
                        print(f'У игрока {hero1} теперь столько денег: {hero1.money}')
                        break
    def upgrade_your_hero(self,  current_castle):
        
        self.current_castle = current_castle
        if self.current_castle.money > 100000:
            self.hp += 5000
            self.dmg += 2000
            self.current_castle.money -= 100000
            print(f'Теперь хп вашего героя {self.hp}, а урон {self.dmg}')
            print(f'У вас осталось {self.current_castle.money} денег')
        else:
            print(f'Вам не хватает {100000-self.current_castle.money}')
        
        


hero = Hero('lol')
# hero.attack_npc(skeleton, 20, red)

# # hero1 = Hero('hero1')
# # hero2 = Hero("hero2")
# hero.army_attack_player(red, green)

# red.army_creation("Human", 150)
# hero.army_attack_npc('Dragon',20 , red, skeleton)
# hero = Hero('adad')
# hero.attack_npc(dragon, 80800, red)
hero.upgrade_your_hero(red)
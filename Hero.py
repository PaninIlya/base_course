from NPC import NPC 
from NPC import skeleton, dragon, goblin
from Army import Army
from Castle import Castle, red, green


class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 1000
        self.dmg =600
        self.army = {'Human': 0, 'Giant': 0, 'Canon': 0}
        self.army_dmg = 0
        self.army_hp = 0
    

    def attack_npc(self , npc, current_castle, kol):
        self.npc = npc
        self.current_castle = current_castle
        self.kol = kol
        if self.hp >  npc.dmg and self.dmg > npc.hp:
            npc.hp = 0
            self.hp -= npc.dmg
            current_castle.money += npc.price * self.kol
            print(f'Ваш герой убил {self.kol} {npc}(ов)')
            print(f"Ваше кол-во денег : {current_castle.money}")
        else:
            print('Ваш герой недстаточно силен')


    def army_attack_npc(self, type, kol,current_castle, npc):
        self.type = type
        self.kol = kol
        hp = current_castle.hp + self.hp
        
        if hp > npc.dmg * self.kol:
            print(f'Castle {self.hp}')
            hp -= npc.dmg * self.kol
            print(f"Вы убили {npc}")

        else:
            print('Ваша армия слишком слаба')

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


                             ''')
                        hero1.hp = 0
                        print(f"у армии замка {hero1} остлось {hero1.hp} здоровья")
                        break
                    elif hero2.hp <= 0:
                        print(f'''
                             ============================== 
                              Победила армия игрока {hero1}
                             ==============================


                            ''')
                        hero2.hp = 0
                        print (f"у армии замка {hero2} осталось {hero2.hp} здоровья")
                        break
        
        
        


hero = Hero('lol')
hero.attack_npc(skeleton, red, 20)

# hero1 = Hero('hero1')
# hero2 = Hero("hero2")
hero.army_attack_player(red, green)

# red.army_creation("Human", 150)
# hero.army_attack_npc('Dragon',20 , red, skeleton)
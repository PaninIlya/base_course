from NPC import NPC 
from NPC import skeleton, dragon, goblin

class Hero:
    def __init__(self,color):
        self.color = color
        self.hp = 1000
        self.dmg =600
        self.army = {'Human': 0, 'Giant': 0, 'Canon': 0}
        self.army_dmg = 0
        self.army_hp = 0
    

    def attack_npc(self , npc):
        if self.hp >  npc.dmg and self.dmg > npc.hp:
            npc.hp = 0
            self.hp -= npc.dmg
            print(f'Ваш герой убил {npc}')
        else:
            print('Ваш герой недстаточно силен')

hero = Hero('lol')
hero.attack_npc(skeleton)
hero.attack_npc(dragon)
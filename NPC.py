def npc_stats():
    print(f'''  
               ===================================================================
               |      Скелет        |         Гоблин      |         Дракон       |  
               |==================================================================
               |                    |                     |                      |                     
               |hp = {skeleton.hp}  |  hp = {goblin.hp}   |  hp = {dragon.hp}    |  
               |                    |                     |                      |                    
               |dmg = {skeleton.dmg}|  dmg = {goblin.dmg} |  dmg = {dragon.dmg}  |   
               |==================================================================
          
          
          ''')

class NPC:

    def __init__ (self, type):
        self.type = type
        npc = {'skeleton': 0, 'goblin': 0, 'dragon': 0}
        if self.type == 'skeleton':
            self.hp = 50
            self.dmg = 25
        elif self.type == 'goblin':
            self.hp = 150
            self.dmg = 75
        elif self.type == 'dragon':
            self.hp = 600
            self.dmg = 350

    def __str__(self):
        return self.type
    

skeleton = NPC('skeleton')
goblin = NPC('goblin')
dragon = NPC('dragon')

stats = npc_stats()
print(stats)
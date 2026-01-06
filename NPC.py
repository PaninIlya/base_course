

class NPC:

    def __init__ (self, type, dmg , hp, price):
        self.type = type
        self.dmg = dmg
        self.hp = hp
        self.price = price
        # npc = {'skeleton': 0, 'goblin': 0, 'dragon': 0}
    

    @staticmethod
    def npc_stats():
        print(f'''  
                ===================================================================
                |      Скелет        |         Гоблин      |         Дракон       |  
                |==================================================================
                |                    |                     |                      |                     
                |    hp = {skeleton.hp}        |       hp = {goblin.hp}      |        hp = {dragon.hp}     |     
                |                    |                     |                      |                    
                |    dmg = {skeleton.dmg}        |       dmg = {goblin.dmg}     |        dmg = {dragon.dmg}     |     
                |==================================================================
            
            
            ''')


    def __str__(self):
        return self.type
    

skeleton = NPC('skeleton', 50, 100, 250)
goblin = NPC('goblin', 100, 250, 400)
dragon = NPC('dragon', 500, 1000, 5000)

NPC.npc_stats()
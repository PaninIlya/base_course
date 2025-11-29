color_list = {1:'Red',2:'Yellow',3:'Green',4:'Blue'}
warriors_list = {1:"Human", 2:"Giant", 3:"Archer"}
class Warrior:
    def __init__ (self,type, index):
        
        self.type = type
        self.index = index
        if self.type == "Human":
            self.hp = 50
            self.dmg = 25
            self.price = 25
        elif self.type == "Giant":
            self.hp = 500
            self.dmg = 250
            self.price = 300
        elif self.type == "Archer":
            self.hp = 45
            self.dmg = 80
            self.price = 80




class NPC:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

skeleton = NPC(20, 10)
dragon = NPC(500, 200)
goblin = NPC(50, 450)




class Castle:
    def __init__ (self, index):
        self.index = index
        self.hp = 100000
        self.money = 1000000
        self.army = []
        self.upg_price = 50000
        self.army_dmg = 0
        self.army_hp = 0
        
    def buy_army(self):
        while True:
            print(f'Ваши деньги:{self.money}')
            self.choice = int(input(f"Кого вы хотите купить(Выберите цифру)?:{warriors_list}:\n"))
            if self.choice == 0:
                break
            self.kol = int(input('Сколько ?:'))
            if self.kol == 0:
                break
            if self.money >= Warrior(warriors_list[self.choice], 1).price * self.kol:
                for i in range(self.kol):
                    self.army.append(Warrior(warriors_list[self.choice], i+1))
                    self.money -= Warrior(warriors_list[self.choice], 1).price
                print(f'Осталось денег:{self.money}')
                print(f'Ваша армия: {self.army}')
                
            else:
                print('Недостаточно денег!')
                break
            for i in range(len(self.army)):
                self 


    def upg(self):
        if self.money > self.upg_price:
            self.hp += 50000
            self.money -= self.upg_price
            print(f'У вас осталось денег : {self.money}')
            print(f'Хп вашего замка теперь = {self.hp}')
        else:
            print('У вас недостаточно денег')

     

red_castle = Castle(1)
yellow_castle = Castle(2)
green_castle = Castle(3)
blue_castle = Castle(4)           

class Hero:
    def __init__(self, index, castle):
        self.index = index
        self.hp = 500
        self.dmg = 400
        self.army = []
        self.castle = castle
        self.upg_price = 10000


    def hero_upg(self):
        if self.castle.money > self.upg_price:
                self.castle.money -= self.upg_price
                self.hp += 200
                self.dmg += 400
                print(f'Теперь хп вашего героя {self.hp}, а урон {self.dmg}')
                print(f'У вас осталось денег : {self.castle.money}')
        else:
            print('У вас не хватает денег')


    def attack_npc(self):
        wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
        while wish == 'Да':
            npc_selector = input('Кого хотите атаковать?(skeleton/dragon/goblin):')
            if npc_selector == 'skeleton':
                self.hp -= skeleton.dmg
                skeleton.hp -= self.dmg
                if skeleton.hp <= 0:
                    skeleton.hp = 0
                    self.castle.money += 100
                    print('Ваш герой убил скелета')
                    
                    if self.hp <= 0:
                        self.hp = 0
                        self.death()

                        break
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
                else:
                    print('Ваш герой недостаточно силён ,чтобы убить его')
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
            if npc_selector == 'dragon':
                self.hp -= dragon.dmg
                dragon.hp -= self.dmg
                if dragon.hp <= 0:
                    dragon.hp = 0
                    self.castle.money += 25000
                    print('Ваш герой убил дракона')
                    
                    if self.hp <= 0:
                        self.hp = 0
                        self.death()
                        break
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
                   
                else:
                    print('Ваш герой недостаточно силён ,чтобы убить его')
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
            if npc_selector == 'goblin':
                self.hp -= goblin.dmg
                goblin.hp -= self.dmg
                if goblin.hp <= 0:
                    goblin.hp = 0
                    self.castle.money += 200
                    print('Ваш герой убил гоблина')
                    
                    if self.hp <= 0:
                        self.hp = 0
                        self.death()
                        break
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
                else:
                    print('Ваш герой недостаточно силён ,чтобы убить его')
                    wish = input('Хотите ли вы атаковать NPC?(Да/Нет):')
            if self.hp <= 0:
                self.hp = 0
                print('Хп вашего героя 0')
            if self.hp > 0:
                print(f'Хп вашего героя {self.hp}')
            if wish == 'Нет':
                break


    def death(self):
        print('Ваш герой умер, но вы получите нового(но без усилений)')
        self.hp = 500
        self.dmg = 400
    


        

      


red_hero = Hero(1, red_castle)
yellow_hero = Hero(2, yellow_castle)
green_hero = Hero(3, green_castle)
blue_hero = Hero(4, blue_castle)

red_hero.attack_npc()

class Player:    
    def __init__ (self,color, castle, hero):
        self.color = color
        self.castle = castle
        self.hero = hero


    def buy_army(self):
        if self.color == 1:
            red_castle.buy_army()

        elif self.color == 2:
            yellow_castle.buy_army()
        elif self.color == 3:
            green_castle.buy_army()
        elif self.color == 4:
            blue_castle.buy_army()


    def castle_upg(self):
        wish = input(f'Хотите ли улучшить свой замок за {self.castle.upg_price}?(Да/Нет )')
        if wish == 'Да':
            self.castle.upg()
        elif wish == 'Нет':
            print('Замок остался прежним')


    def hero_upg(self):
        wish = input(f'Хотите ли вы улучшить героя за {self.hero.upg_price}?(Да/Нет)')
        if wish == 'Да':
            self.hero.hero_upg()
        elif wish == 'Нет':
            print('Герой остался без измений')

    
    def new_hero(self):
        if self.hero.hp <= 0:
            self.hero.death()
            
        else:
            print('Ваш герой еще жив')


red_player = Player(1, red_castle, red_hero)
yellow_player = Player(2, yellow_castle, yellow_hero)
green_player = Player(3, green_castle, green_hero)
blue_player = Player(4, blue_castle, blue_hero)

red_player.buy_army()
red_player.castle_upg()
red_player.hero_upg()
red_player.new_hero()
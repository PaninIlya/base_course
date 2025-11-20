color_list = ["Red", "Yellow", "Green", "Blue"]
warriors_list = ["Human", "Goblin", "Dragon"]
class Warrior:
    def __init__(self, type, index):
        self.type = type
        self.index = index
        if self.type == "Human":
            self.hp = 50
            self.dmg = 25
            self.price = 25
        elif self.type == "Goblin":
            self.hp = 75
            self.dmg = 30
            self.price = 40
        elif self.type == "Dragon":
            self.hp = 600
            self.dmg = 400
            self.price = 2500


# class Goblin:
#     def __init__(self, index):
#         self.index = index
#         self.hp = 75
#         self.dmg = 30
#         self.price = 40



# class Dragon:
#     def __init__(self, index):
#         self.index = index
#         self.hp = 600
#         self.dmg = 400
#         self.price = 2500


class Castle:
    def __init__(self, index):
        self.index = index
        self.hp = 10000
        self.money = 5000
        self.army = []


class Player:
    def __init__(self,color):
        self.color = color
        print(f'Ваш цвет - {color_list[self.color-1]}, Вы  - Player({self.color})')
    def buy_army(self):
        for i in range(3):
            print(f'Ваши деньги:{Castle(self.color).money}')
            self.choice = input(f"Кого вы хотите купить?:{warriors_list}:\n")
            if self.choice == "0":
                break
            self.kol = int(input("Какое количетство?: "))
            if Castle(self.color).money >= Warrior(self.choice,1).price * self.kol:
                print("Успешно!")
                Castle(self.color).army.append(Warrior(self.choice,i+1))
                Castle(self.color).money -= Warrior(self.choice,1).price * self.kol
                print(f'Осталось денег:{Castle(self.color).money}')
                print(f'Осталось денег:{Castle(self.color).money - Warrior(self.choice,1).price}')
            else:
                print("Недостаточно денег!")
                break

class Hero:
    def __init__(self,index):
        self.index = index
        self.hp = 500
        self.dmg = 50
    

player = Player(int(input(f"Выберите номер цвета игрока:{color_list}: ")))
player.buy_army()
print(Castle(3).army)




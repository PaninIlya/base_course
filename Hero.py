from NPC import NPC 
from NPC import skeleton, dragon, goblin
from Army import Army
from Castle import *
import time

def start_hero_stats():
     print(f'''
            
            ХП: 10000
            Урон: 1500

        ''')

def timer_decorator(func):
    """Измеряет время  боя"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        duration = end_time - start_time
        print(f"Бой длился: {duration:.2f} секунд")
        
      
        
        return result
    return wrapper
     

def decorator_attack_player(func):
    def wrapper(self, castle1, castle2):
        print(f'\n{"⋈"*50}')  
        print('             Игроки вступили в бой!')
        print(f'                {castle1.color} vs {castle2.color}')
        print(f'{"⋈"*50}')  
        result = func(self, castle1, castle2)
        print(f'{"⋈"*50}')
        print('             Бой закончен!')
        print(f'{"⋈"*50}')
        return result
    return wrapper


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
            print(f"Вы убили {self.kol} {npc}")
            print(f'Ваши деньги: {current_castle.money}')

        else:
            print(f'Ваша армия слишком слаба для атаки {self.kol} {self.npc}')

    

    @timer_decorator
    @decorator_attack_player
    def army_attack_player(self, castle1, castle2):
        round_num = 1
        
        
        castle1_hp = castle1.hp
        castle2_hp = castle2.hp
        
        print(f"\nНачало битвы!")
        print(f"{castle1.color}: {castle1_hp} HP, Урон: {castle1.dmg}")
        print(f"{castle2.color}: {castle2_hp} HP, Урон: {castle2.dmg}")
        
        while castle1_hp > 0 and castle2_hp > 0:  
            print(f"\n{'='*40}")
            print(f"Раунд {round_num}")
            print(f"{'='*40}")
            
            
            time.sleep(0.8)
            damage1 = castle1.dmg
            castle2_hp -= damage1
            print(f"⚔️  {castle1.color} атакует на {damage1} урона!")
            print(f"❤️  У {castle2.color} осталось {max(castle2_hp, 0)} HP")
            
            if castle2_hp <= 0:
                time.sleep(0.8)
                print(f"\n💥 {castle2.color} уничтожен!")
                break
            
            
            time.sleep(0.8)
            damage2 = castle2.dmg
            castle1_hp -= damage2
            print(f"⚔️  {castle2.color} атакует на {damage2} урона!")
            print(f"❤️  У {castle1.color} осталось {max(castle1_hp, 0)} HP")
            
            if castle1_hp <= 0:
                time.sleep(0.8)
                print(f"\n💥 {castle1.color} уничтожен!")
                break
            
            round_num += 1
            time.sleep(1.0)  
        
        
        time.sleep(1.0)
        print(f"\n{'='*50}")
        print("Битва окончена")
        print(f"{'='*50}")
        
        if castle1_hp <= 0 and castle2_hp <= 0:
            print("🏳️ НИЧЬЯ! Оба замка уничтожены!")
            castle1.hp = 0
            castle2.hp = 0
            
        elif castle1_hp <= 0:
            print(f"🎉 ПОБЕДИТЕЛЬ: {castle2.color}!")
            print(f"🏆 {castle1.color} проиграл")
            
            
            castle1.hp = 0
            castle2.hp = max(castle2_hp, 0)
            
            
            castle2.money += castle1.money
            castle1.money = 0
            
            print(f"💰 {castle2.color} получает все деньги {castle1.color}!")
            
        else:  
            print(f"🎉 ПОБЕДИТЕЛЬ: {castle1.color}!")
            print(f"🏆 {castle2.color} проиграл")
            
            
            castle2.hp = 0
            castle1.hp = max(castle1_hp, 0)
            
            
            castle1.money += castle2.money
            castle2.money = 0
            
            print(f"💰 {castle1.color} получает все деньги {castle2.color}!")
        
        
        time.sleep(0.8)
        print(f"\n📊 Итоги боя:")
        print(f"{'-'*30}")
        print(f"{castle1.color}:")
        print(f"  HP: {castle1.hp}")
        print(f"  Деньги: {castle1.money}")
        print(f"{castle2.color}:")
        print(f"  HP: {castle2.hp}")
        print(f"  Деньги: {castle2.money}")
        
        return True

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
# hero2 = Hero('lol2')
# # hero.attack_npc(skeleton, 20, red)

# # # castle1 = Hero('castle1')
# # # castle2 = Hero("castle2")
# hero.army_attack_player(red, green)

# red.army_creation("Human", 150)
# hero.army_attack_npc('Dragon',20 , red, skeleton)
# hero = Hero('adad')
# hero.attack_npc(dragon, 80800, red)
# hero.upgrade_your_hero(red)
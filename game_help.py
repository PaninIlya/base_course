def help():
    print(f"""
          класс Castle: принимает цвет(или ник)
            методы класса Castle: 
                                army_creation(тип, количество) (типы: Human , Giant, Canon)
          
                                upgrade_your_castle(можно прокачать свой замок за 100000)
          

          класс Hero: принимает цвет(или ник)
            методы класса Hero: 
                               attack_npc(тип нпс(skeleton, dragon, goblin), кол-во нпс, замок игрока) - сам герой атакует нпс

                               army_attack_npc(тип нпс(skeleton, dragon, goblin), кол-во нпс, замок игрока) - армия атакует нпс

                               army_attack_player(замок игрока 1, замок игрока 2) - атака других игроков (принимает на вход названия замков)
          
          
          класс NPC: объекты класса (skeleton ,dragon, goblin) уже созданы

          класс Army: объекты класса (Human, Giant, Canon) уже созданы
          
          
          """)
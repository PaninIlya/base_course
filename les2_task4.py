class Planet:
    planet_count = 0
    krutii_planeti = 0

    def __init__(self, age):
        self.age = age

    @staticmethod
    def stepen_krutosti(stepen):
        if stepen > 52:
            print('\nПланета крутая')
            Planet.planet_count += 1
            Planet.krutii_planeti += 1
           
            return True
        else:
            print('\nПланета не оч крутая')
            Planet.planet_count += 1
            # print(f'Всего планет: {Planet.planet_count}')
            return False
        

    @classmethod
    def krutii_plt(cls):
        print(f'\nВсего планет : {cls.planet_count}')
        print(f'\nКрутых планет : {cls.krutii_planeti}')
    
    @property
    def age_checker(self):
        if self.age >= 4500000000:
            print('\nПланета старая')
        elif 0< self.age < 4500000000:
            print('\nПланета молодая')
        else:
            print('\nВы ввели некорректный возраст')

Planet.stepen_krutosti(69)
Planet.stepen_krutosti(42)
Planet.stepen_krutosti(8888)

Planet.krutii_plt()

pl1 = Planet(999999999999)
pl2 = Planet(50)
pl1.age_checker
pl2.age_checker
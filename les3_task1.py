# class Entrepreneur:

#     def __init__(self, name, age, capital , business):
#         self.name = name
#         self.age = age
#         self.capital = capital
#         self.business = business


#     def get_info(self):
#         print(f'''Имя: {self.name} ,
#                Возраст: {self.age}, 
#                Капитал: {self.capital}, 
#                Бизнес: {self.business}''')


#     def earn_money(self, money_amount):

#         self.money_amount = money_amount

#         if self.money_amount > 0:
#             self.capital += self.money_amount
#             print(f'{self.name} заработал {self.money_amount}, теперь капитал  = {self.capital}')
#         else:
#             print(f'{self.name} не заработал денег :(')
    

#     def buy_bussiness(self, cost):
#         self.cost = cost

#         if self.capital >= self.cost:
#             self.capital -= self.cost
#             print(f'{self.name} приобрел бизнес за {self.cost}, капитал после покупки равен {self.capital}')
        
#         else:
#             print(f'У {self.name} недостаточно денег для покупки бизнеса за {self.cost}')

class Business:


    def __init__(self, _area='Ресторан', _price= 5000000):
        self._area = _area
        self._price = _price


    def final_price(self, discount):
        self.discount = discount
        final_price = self._price - (self._price * (self.discount/100))

        return final_price
    

class Businessman:

    def_name = 'Вася'
    def_age = 67


    def __init__(self, name=def_name, age=def_age):
        self.name = name
        self.age = age

        self._money = 0
        self._buisiness = None
    

    def info(self):
        print(f''' 
                Имя : {self.name}
                Возраст: {self.age}
                Деньги: {self._money}
                Бизнес: {self._buisiness}
                ''')


    @staticmethod
    def def_info():
        print(f'''Имя: {Businessman.def_name}
                  Возраст : {Businessman.def_age}
                    ''')
    
    def _make_deal(self, object, cost):
        self.cost = cost
        self.object = object

        self._money -= self.cost
        self._buisiness = self.object
    

    def earn_money(self, money_amount):
        self.money_amount = money_amount

        self._money += self.money_amount


    def buy_business(self, business, discount):
        self.business = business
        self.discount = discount
        final_price = self.cost - (self.cost * (self.discount/100))

        if self._money > final_price:
             self._make_deal(business, final_price)
             print(f'''{self.name} успешно приобрел бизнес за {final_price}''')
        else:
            print(f'У {self.name} недостаточно денег, чтобы купить бизнес')



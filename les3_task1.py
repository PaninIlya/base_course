
class Business:


    def __init__(self, _area=600, _price= 5000000):
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
        self._business = None
    
    
    def info(self):
        print(f''' 
                Имя : {self.name}
                Возраст: {self.age}
                Деньги: {self._money}
                Бизнес: {self._business}
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
        self._business = self.object
    

    def earn_money(self, money_amount):
        self.money_amount = money_amount

        self._money += self.money_amount


    def buy_business(self, business, discount):
        self.business = business
        self.discount = discount
        final_price = business.final_price(discount)

        if self._money > final_price:
             self._make_deal(business, final_price)
             print(f'''{self.name} успешно приобрел бизнес за {final_price}''')
        else:
            print(f'У {self.name} недостаточно денег, чтобы купить бизнес')


class RestarauntBusiness(Business):
    def __init__(self, _price):
       self.profitability = 50000000
       super().__init__(_area = 500, _price = _price)




Businessman.def_info()

vasa = Businessman('Петя', 56565)
vasa.info()

pizza = RestarauntBusiness(5000000)


vasa.buy_business(pizza, 50)
vasa.earn_money(999999999999999)
vasa.buy_business(pizza, 50)
vasa.info()
class Wallet:
    def __init__(self, moeny):
        self.money = moeny
    
    def __add__(self, other):
        return self.money + other.money
    
    def __radd__(self, other):
        return self.money + other
    
    def __iadd__(self, other):
        self.money += other.money
        return self
    
    def __eq__(self, other):
        return self.money == other.money
    
    def __ne__(self, other):
        return self.money != other.money
    
    def __len__(self):
        return self.money // 1000 #кол-во 1000рублевых купюр
    
    def __sub__(self, other):
        return self.money - other.money
    
    def __rsub__(self, other):
        return other - self.money
    
    def __isub__(self, other):
        self.money -= other.money
        return self
    
    def __mul__(self, other):
        return self.money * other.money
    
    def __rmul__(self, other):
        return self.money * other
    
    def __truediv__(self, other):
        return round(self.money/other.money)
    
    def __bool__(self):       
        return self.money > 0
    
    def __repr__(self):      
        return f"Wallet: {self.money}"
    
w1 = Wallet(500000)
w2 = Wallet(4000)
print(len(w1))
print(bool(w1))
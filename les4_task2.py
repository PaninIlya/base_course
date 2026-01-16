class Cell:

    def __init__(self, kol):
        self.kol = kol
    
    def __add__(self, other):
        print('add:', self.kol, other.kol)
        return self.kol + other.kol
    
    def __sub__(self, other):
        print('sub:', self.kol, other.kol)
        return self.kol - other.kol

    def __mul__(self, other):
        print('mul:', self.kol, other.kol) 
        return self.kol * other.kol


    def __truediv__(self, other):
        print('truediv:', self.kol, other.kol)
        return round(self.kol/other.kol)   
genadiy = Cell(100)
bobik = Cell(15)
b = genadiy + bobik
c = genadiy * bobik
g = genadiy/bobik
print(b)
print(c)
print(g)
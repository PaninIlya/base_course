class Number1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val
    
    def __sub__(self, other):
        print('sub', self.val, other)
        return self.val - other
       
    def __rsub__(self, other):
        print('rsub', self.val, other)
        return other - self.val
    
    def __isub__(self, other):
        print('isub', self.val, other)
        self.val -= other
        return self
    
x = Number1(20)
y = Number1(30)
print(1 + x)
print(x + 1)
x -=1
print(x)
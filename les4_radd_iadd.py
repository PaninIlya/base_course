class Number1:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    #__radd__ = __add__

    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val
        #return self.__add__(other)
        #return self.val + other

x = Number1(20)
y = Number1(30)
print(1 + x)
print(x + 1)
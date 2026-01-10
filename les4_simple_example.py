class Number:
    def __init__(self, value):
        self.data = value

    
    def __add__(self, other): #сложение справа
        return Number(self.data + other.data)
    

a = Number(12)
c = Number(4)
b = a + c
print(b.data)
# class Number:
#     def __init__(self, value):
#         self.data = value

    
#     def __add__(self, other): #сложение справа
#         return Number(self.data + other.data)
    

# a = Number(12)
# c = Number(4)
# b = a + c
# print(b.data)
import numpy as np
a = 'Good'
b = [1,4,6]
c = 3
d = 4.3
e = np.zeros(5)
f = {'a':4, 'b':5}
g = (1,6,7)
print(dir(a))
print()
print(dir(b))
print()
print(dir(g))
print()
def fun():
    pass

class A:
    pass
aA = A()
print(dir(dir))
# print()
# print(dir(A))
# print()
# print(dir(aA))
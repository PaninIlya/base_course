def changer(a: int, b: list):
    a = 2
    b[0] = 'Good'

x = 10
y = [1, 2]

changer(x, y)
print(x) 
print(y)
y = [1, 2]

changer(x, y[:])
print(y)

a = 3
def func(a):
    a = 5
    print(a, id(a))


func(a)
print(a, id(a))

b = 7


def global_func():
    print(b**2)

global_func()
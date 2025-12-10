import time
a = 2
b = 3
c = 4
d = 5
e = 3
n = 10**5

timer1 = time.time()


def cycle_checker():
    list1 = []
    for x in range(n):
        list1.append(a*x**4 + b*x**3 + c**x*2 + d*x + e)
    print(time.time()-timer1)
    return list1


cycle_checker()

timer2 = time.time()


def list_add():
    list2 = [a*x**4 + b*x**3 + c**x*2 + d*x + e for x in range(n)]
    print(time.time()-timer2)
    return list2


list_add()

timer3 = time.time()

def map_checker(x):
    
    return a*x**4 + b*x**3 + c**x*2 + d*x + e

kol = range(n)
list3 = list(map(map_checker, kol))

print(time.time()- timer3)
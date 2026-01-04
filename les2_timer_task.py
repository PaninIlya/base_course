import time
def timer_decorator(func):
    def fnc():
        timer = time.time()
        func()
        print(f'Функция работала {time.time() - timer} секунд')
    return fnc

@timer_decorator
def chto():
    n = 5
    while n != 0:
        n -=1
        print(n)

chto()

@timer_decorator
def addition():
    list = []
    for i in range(10):
        list.append(2)
    print(list)

addition()
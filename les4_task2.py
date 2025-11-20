import numpy as np



el = int(input(f'Введите кол-во элементов'))
mas = np.zeros((el))

for i in range(el):
        mas[i] = int(input(f'Заполните массив, элемент с индексом: [{i}]'))

def proizv(mas):
        a = 1

        for z in range(el):
                a *= mas[z]
        print(a)

        

proizv(mas)

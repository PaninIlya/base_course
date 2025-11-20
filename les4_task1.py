import numpy as np

stroki = int(input(f'Введите кол-во строчек'))
mas = np.zeros((stroki))

for i in range(stroki):
        mas[i] = int(input(f'Заполните массив, элемент с индексом: [{i}]'))

def middle(mas):
        print(sum(mas)/len(mas))
        

middle(mas)

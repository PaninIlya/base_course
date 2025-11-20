import numpy as np

stroki = int(input(f'Введите кол-во строчек'))
a = np.zeros((stroki))

for i in range(stroki):
        a[i] = int(input(f'Заполните массив, элемент с индексом: [{i}]'))

def middle(a):
        print(sum(a)/len(a))
        

middle(a)

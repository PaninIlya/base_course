import numpy as np
n = int(input('Введите кол-во элементов массива а: '))
m = int(input('Введите кол-во элементов массива b: '))
j = int(input('Введите кол-во элементов массива c: '))

a = np.zeros(n)
b = np.zeros(m)
c = np.zeros(j)

for i in range(n):
    a[i] = int(input(f'Введите {i+1} элемент массива a: '))

for i in range(m):
    b[i] = int(input(f'Введите {i+1} элемент массива b: '))

for i in range(j):
    c[i] = int(input(f'Введите {i+1} элемент массива c: '))

print(a)
print(b)
print(c)

print(f" Максимальный элемент:{max( max(a), max(b), max(c))}")
print(f'Сумма элементов массива a : {sum(a)}')
print(f'Сумма элементов массива b : {sum(b)}')
print(f'Сумма элементов массива c : {sum(c)}')
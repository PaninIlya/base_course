import numpy as np

n = int(input(f"Введите кол-во строчек: "))
m = int(input(f"Введите кол-во столбцов: "))

a = np.zeros((n, m))
for i in range (n):
    for j in range(m):
        a[i, j] = int(input(f"Заполните число [{i}, {j}]: "))

print(a)

for i in range(m):
    slice = a[::, i]
    max = np.max(slice)
    print(f'Максимальное значение в {i} столбце:{max}')

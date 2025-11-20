import numpy as np

N = int(input("Введите кол-во строчек массива:"))
M = int(input("Введите кол-во столбцов массива:"))

trigonometry_array = np.zeros((N, M))
for i in range(N):
    for j  in range(M):
        el = np.sin(N * i + M * j + 1)
        if el <0:
            trigonometry_array[i, j] = 0
        else:
            trigonometry_array[i, j] = el

print(trigonometry_array)
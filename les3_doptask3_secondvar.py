import numpy as np

n = int(input(f"Введите кол-во строчек: "))
m = int(input(f"Введите кол-во столбцов: "))

a = np.zeros((n, m))
for i in range (n):
    for j in range(m):
        a[i, j] = int(input(f"Заполните число [{i}, {j}]: "))

print(a)

m_list = []
max = -999

for j in range(m):
    for z in range(n):
        for i in range(n):
            if a[i, j] > max:
                max = a[i, j]
    m_list.append(int(max))
    max = -1
    
print(m_list)
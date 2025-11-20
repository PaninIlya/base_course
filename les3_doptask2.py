import numpy as np


a = np.ones((5))

for i in range(5):
    a[i] = int(input(f"Заполните массив: число{i+1} "))


print(a)

c = int(input("Введите само число:"))
b = int(input("Введите позицию для нового числа:"))

new_a = np.ones((6))
new_a[b] = c

for i in range(b, 5):
    new_a[i+1] = a[i]

print(new_a)

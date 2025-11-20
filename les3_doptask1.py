import numpy as np

a1 = np.zeros((2,3))
a2 = np.zeros((2,3))
a3 = np.zeros((2,3))

for i in range(2):
    for z in range(3):
        a1[i, z] = int(input(f"Заполните первый массив[{i} , {z}]:"))
        a3[i, z] = a1[i, z]
      
for i in range(2):
    for z in range(3):
        a2[i, z] = int(input(f"Заполните второй массив [{i}, {z}]"))
        if a3[i, z]<a2[i, z]:
            a3[i,z] = a2[i, z]



print(a1)
print(a2)
print(a3)


import random

print(dir(random))
value = random.randint(1, 6)
print("На кубике выпало:", value)

for i in range(3):
    print(random.random())
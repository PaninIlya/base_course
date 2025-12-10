import random

flowers = ['rose', 'tulip', 'daffodil']
color = ["red", 'blue', 'green', 'yellow', 'white']
color2 = []

for i in range(len(color)):
    color2.append(color[random.randint(0, len(color)-1)])

slovar = dict(zip(flowers, color2))
print(slovar)
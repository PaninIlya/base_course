import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]

plt.plot(x, y, color = 'g', label = 'Graf 1', marker = '>', ms = 5) #ms - marker size(в процентах по отношению  размеру графика)
plt.plot(y, x, color = 'r', label = 'Graf 2', marker = 'o', ms = 3)

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend() #окошко, куда вставляются лейблы
plt.grid() # Создние сетки
plt.title('Base')

plt.savefig('lol.png')
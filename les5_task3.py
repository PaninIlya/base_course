numbers = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]

cubik = list(map(lambda x: x ** 3 if x % 2 == 0 else x, numbers))
print(cubik)
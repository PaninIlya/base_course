# Команды для поиска минимального и максимального значений

values = [-43, 34.453, 45, 3.43e3, 0xABBA, 0b010111001]
print(values)

print('minimum:', min(values))
print('maximum:', max(values))


def avg(l):
    return sum(l) / len(l)


print('average:', avg(values))
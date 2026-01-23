def sq(chislo):
    yield chislo**2

num = sq(5)
print(next(num))


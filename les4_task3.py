import les4_const as l4


def energy(m, h, U):
    Ek = m*U**2/2
    Ep = m*l4.g*h
    E = Ek+Ep
    return E
m = int(input('Введите массу тела:'))
h = int(input('Введите высоту:'))
U = int(input('Введите скорость:'))

E = energy(m, h, U)
print(E)
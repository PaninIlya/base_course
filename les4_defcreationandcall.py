def mult_func(a):
    x = 3 * a
    return x


def my_print(a):
    print(f'Это мой принт с блэкджэком и {a}')


tmp = mult_func(4)
print(tmp)

print(mult_func(10))

print(mult_func('Good'))
my_print('Hello')
my_print(mult_func('50'))

# def sum_arg(a,b):#Именованная функция
#     return a + b

# print(sum_arg(12, 25))

# #lambda аргумент1, арг2 и тд: выражение, использующее аргументы

# sum_arg = lambda a, b: a + b#Анонимная функция

a_list = [lambda a,b: f'a: {b**2}' for _ in range(100)]
print(a_list[0](1,5))
def decorator(func):
    print('Hello World!')
    return func

@decorator#надстройка над функцией (дали ей доп функционал)
def decorate_example():
    print('Привет , Вселенная!')


decorate_example()

#другое объявление декоратора
decorate_example = decorator(decorate_example) # = @decorator
decorate_example()
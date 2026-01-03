def decorator(n):
    def f(func):
        def decorator2(n2):
            print(n + func(n2))
        return decorator2
    return f

@decorator(9)
def s(n2):
    return n2

s(100)
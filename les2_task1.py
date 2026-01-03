def decorator(n):
    def f(func):
        def f2(n2):
            print(n + func(n2))
        return f2
    return f

@decorator(9)
def s(n2):
    return n2

s(100)
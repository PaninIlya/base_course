def decorator(n):
    def wrapper(func):
        def chislo(x):           
            result = n + func(x)
            return result
        return chislo
    return wrapper

@decorator(100)  
def get_number(x):
    return x  

print(get_number(89))  
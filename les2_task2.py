def decorator(func):
    def f(n1, n2, math_sign):
        if math_sign == '+':
            print(n1 + n2)
            return n1 + n2
        elif math_sign == '*':
            print(n1 * n2)
            return n1 * n2
        elif math_sign == '/':
            print(n1/n2)
            return n1 / n2
        elif math_sign == '-':
            print(n1-n2)
            return n1 - n2
        
    return f

@decorator
def two_variables(n1, n2, math_sign):
    return two_variables

two_variables(1, 2 ,'/')
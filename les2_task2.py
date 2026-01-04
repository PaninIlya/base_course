def calculator(func):
    def wrapper_f(n1, n2, math_sign):
        if math_sign == '+':
            print(n1 + n2)
            
        elif math_sign == '*':
            print(n1 * n2)
            
        elif math_sign == '/':
            print(n1/n2)
            
        elif math_sign == '-':
            print(n1-n2)  
    return wrapper_f

@calculator
def two_variables(n1, n2, math_sign):
    return n1, n2, math_sign

two_variables(1, 2 ,'/')
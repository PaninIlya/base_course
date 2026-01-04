def calculator(func):
    def f(n1, n2, math_sign):
        if math_sign == '+':
            print(n1 + n2)
            
        elif math_sign == '*':
            print(n1 * n2)
            
        elif math_sign == '/':
            print(n1/n2)
            
        elif math_sign == '-':
            print(n1-n2)  
    return f

@calculator
def two_variables(n1, n2, math_sign):
    return n1, n2, math_sign

two_variables(1, 2 ,'/')
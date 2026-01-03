def decorator(func):
    def two_variables(n1, n2, math_sign):
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
        
    return two_variables

@decorator
def nothing(n1, n2, math_sign):
    return nothing

nothing(1, 2 ,'/')
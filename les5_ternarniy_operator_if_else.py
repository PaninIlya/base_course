'''
x = True
if x:
    z = 1
else:
    z =0
z = 1 if x else 0
'''
maximum = (lambda a,b: a if a>b else b)
print(maximum(23, 25))
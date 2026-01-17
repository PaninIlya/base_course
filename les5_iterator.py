f = open('example.txt')
'''
example.txt  example2.txt
x            1
2+x          1+1
'''
#readline - команда для чтения файла построчно
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')

#метод __next__() (тоже самое , но через маг метод)
# print(next(f), end='')
# print(next(f), end='')
# print(next(f), end='')

f2 = open('example2.txt')
for i in f2:#итератор файла
    print(i, end='')


new_f = iter(f)
print(new_f)
f.close()
f2.close()
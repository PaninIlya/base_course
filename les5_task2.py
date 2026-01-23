def cheker():
    n = int(input('Введите число от 1 до 100(целые): '))
    if n < 1 or n > 100:
        print('Вы ввели неверное число!')
        
    return n

def game(first: int, last: int, chislo: int):
    if first == last:
        print(f'Ваше число {first}')
        return  
    
    mid = (last + first) // 2
    print(f'Ваше число больше или равно {mid}?:')
    
    if chislo >= mid:
        print('да')
        game(mid + 1, last, chislo) 
    else:
        print('нет')
        game(first, mid - 1, chislo)  


n = cheker()  
if n:  
    game(1, 100, n)  
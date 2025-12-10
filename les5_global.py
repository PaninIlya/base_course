# global - позволяет локально изменять глобальные переменные
counter = 0

def update(value):
    global counter
    result = counter + value

    print(f"{counter} + {value} = {result}")
    counter = result

update(1)
update(5)
update(3)

print(f"{counter = }")
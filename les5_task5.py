name = 'Panin Ilya Sergeevich'

name_upper = name.upper()
l_up = [i for i in name_upper]

print(l_up)

list_upper = [ord(i) for i in l_up]
print(sum(list_upper))

name_lower = name.lower()
l_low = [i for i in name_lower]


print(l_low)

list_lower = [ord(i) for i in l_low]
print(sum(list_lower))


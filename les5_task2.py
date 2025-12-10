name = 'Panin Ilya'
name_str = '_'.join(name) + '_'
name_up = name_str.upper()
print(name_up)


name_list = [ord(i) for i in name_up ]
print(name_list)

name_str2 = '_'.join(name) + '_'
name_low = name_str2.lower()
print(name_low)

name_list2 = [ord(i) for i in name_low ]
print(name_list2)

print(max(max(name_list), max(name_list2)))
print(min(min(name_list), min(name_list2)))
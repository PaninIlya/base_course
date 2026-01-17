a = range(3)#range допускает множество итераторов(итератор - тот,кто итерирует)
# next(a)
new_a = iter(a)
print(id(new_a))
print(type(new_a))

print(next(new_a))
print(next(new_a))
print(next(new_a))

print(new_a)

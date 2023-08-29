# Вы про это?
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# получите сумму всех чисел,
# распечатайте все строки, где есть буква 'a'

list_one = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

# the way I solve it

print([x for x in list_one if type(x) == str and 'a' in x.lower()])
print(list(filter(lambda x: type(x) == str and 'a' in x.lower(), list_one)))

# the way I would solve in interview :)

new_list = []

for char in list_one:
    if isinstance(char, str) and 'a' in char.lower():
        new_list.append(char)
print(new_list)
from random import randint

names = ['jake', 'sam', 'mark', 'anton']

d = {name:randint(33, 99) for name in names}

passed_d = {k:v for k,v in d.items() if v >= 60}

print(d, passed_d)
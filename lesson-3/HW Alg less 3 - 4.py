""" Task 4. Определить, какое число в массиве встречается чаще всего."""

import random

def get_key(d, value):
    c = []
    for k, v in d.items():
        if v == value:
            c.append(k)
    return c
a = {}
b = []

for f in range(15):
    f = random.randint(1, 30)
    b.append(f)
    
for x in b:
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1

c = get_key(a, max(a.values()))

if len(c) == 1:
    print('Число', end = ' ')
    for x in c:
        print(str(x), end = ' ')
    print('в массиве встречается чаще всего.')
elif len(c) > 1:
    print('Числа', end = ' ')
    for x in c:
        print(str(x), end = ', ')
    print('в массиве встречаются чаще всего.')
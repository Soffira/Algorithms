""" Task 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

b = []

for f in range(7):
    f = random.randint(1, 30)
    b.append(f)

maxim = max(b)
minim = min(b)
v_max = 0
v_min = 0
v = -1
c = 0
for x in b:
    if x == maxim:
        v += 1
        v_max = v
    elif x == minim:
        v += 1
        v_min = v
    else:
        v += 1
        
if v_min + 1 < v_max or v_min > 1 + v_max:
    if v_min + 1 < v_max:
        for r in range((v_max - v_min) - 1):
            c += b[v_min+1]
            v_min += 1
    elif v_min > 1 + v_max:
        for r in range((v_min - v_max) - 1):
            c += b[v_max+1]
            v_max += 1
    print('Сумма элементов в массиве {}, находящихся между минимальным {} и максимальным {} элементами имеет значение {}'.format(b, minim, maxim, c))
else:
    print('Между минимальным: {} и максимальным: {} элементами в массиве {} нет других значений'.format(minim, maxim, b))

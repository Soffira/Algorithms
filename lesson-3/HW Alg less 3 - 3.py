""" Task 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random
a = []
b = []
 
for f in range(10):
    f = random.randint(1, 15)
    b.append(f)
    
maxim = max(b)
minim = min(b)
    
for x in b:
    if x == maxim:
        x = minim
        a.append(x)
    elif x == minim:
        x = maxim
        a.append(x)
    else:
        a.append(x)

print('При смене мест минимальных и максимальных элементов массив {} изменился на {} '.format(b, a))
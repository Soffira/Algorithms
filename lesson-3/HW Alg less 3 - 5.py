""" Task 5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

import random

b = []

for f in range(15):
    f = random.randint(-30, 30)
    b.append(f)

maxim = min(b)
val = []
v = -1
for x in b:
    if x != maxim:
        v += 1
    else:
        v += 1
        val.append(v)

if maxim < 0:
    print('Максимальный отрицательный элемент из массива {} имеет значение {}'.format(b, maxim))
    print('Что соответствует позиции(ям) в массиве:', end = ' ')
    if len(val) > 1:
        for i in val:
            print(i, end = ' ')
    else:
        for i in val:
            print(i)
else:
    print('В массиве нет отрицательных чисел!')

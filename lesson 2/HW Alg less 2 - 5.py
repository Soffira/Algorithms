""" Task 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""

import string
str_lst = string.printable
lst = []
p = 32
w = 0
for z in range(96):
    lst.append(p)
    p += 1

for x in lst:
    for c in range(1):
        print((chr(x) + ' - ' + str(x)), end = ' ')
        w += 1
        if w % 10 != 0:
            continue
        else:
            print('')
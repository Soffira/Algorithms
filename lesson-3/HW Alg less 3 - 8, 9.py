""" Task 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
Task 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

from random import randint
r = 0
c = 0
stroka = 1
M = 5
N = 4
a = []
count = 3
for i in range(N):
    b = []
    for j in range(1):
        for v in range(1):
            q = input(str(stroka) + ' строка. Введите четыре цифры через пробел: ').split(' ')
            for w in q:
                b.append(int(w))
            stroka += 1
        b.append(randint(0, 100))
    a.append(b)
for x in a:
    for z in range(5):
        print(a[r][c], end= ' ')
        c += 1
    print('  |', sum(a[r]))
    r += 1
    c = 0

for i in range(M):
    print("--", end=' ')
print()

min_num = []
lst = []
for i in range(M):
    s = []
    for j in range(N):
        s.append(a[j][i])
    min_num.append(s)
    print(min(min_num[c]), end=' ')
    lst.append(min(min_num[c]))
    c += 1
print()
print('Максимальным элементом среди минимальных элементов столбцов матрицы {} является число {}'.format(lst, max(lst)))

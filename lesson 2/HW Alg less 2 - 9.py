""" Task 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

lst = input('Введите последовательность натуральных чисел через запятую: ').split(',')
lst1 = []
lst2 = []
w = 0
maxim = 1
a = 0
for x in lst:
    for z in x:
        w += int(z)
        if w >= maxim:
            maxim = w
            a = x
        else:
            continue
    lst1.append(int(w))
    w = 0

print('Максимальная сумма числа {} составляет {}'.format(a,maxim))
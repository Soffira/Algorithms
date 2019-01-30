## 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
## Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
from pympler import asizeof
import random
from memory_profiler import profile

def show_sizeof(obj):
    print('Тип: {0}, Размер: {1}'.format(obj.__class__,asizeof.asizeof(obj)))
    
## Task 1
@profile
def game():
    print('Отгадайте число за 3 попыток')
    num = random.randint(0, 100)
    w = 0
    for x in range(3):
        num_choice = int(input('Введите число: '))
        if num_choice == num:
            print('Вы выиграли!')
            break
        elif num_choice > num:
            print('Неверно! Введенное Вами число больше, пропробуйте еще раз: ')
            w += 1
            if w == 3:
                print('Верное число = {}'.format(num))  
        elif num_choice < num:
            print('Неверно! Введенное Вами число меньше, пропробуйте еще раз: ')
            w += 1
            if w == 3:
                print('Верное число = {}'.format(num))

##show_sizeof(num)
##show_sizeof(w)
##show_sizeof(num_choice)

## Task 2            
import string
@profile
def sights():
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

## Task 3
@profile
def resheto():
    n = int(input('Введите число, до которого необходимо посчитать простые числа: '))
    def example2(n):
        a = [0] * n  # создание массива с n количеством элементов
        for i in range(n):  # заполнение массива ...
            a[i] = i  # значениями от 0 до n-1

        # вторым элементом является единица, которую не считают простым числом
        # забиваем ее нулем.
        a[1] = 0

        m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
        while m < n:  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                while j < n:
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1

        # вывод простых чисел на экран (может быть реализован как угодно)
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])

        del a
        
##show_sizeof(str_lst)
##show_sizeof(lst)
##show_sizeof(p)
##show_sizeof(w)

if __name__=="__main__":
    game()

if __name__=="__main__":
    sights()
    
if __name__=="__main__":
    resheto()

''' Python 3.6.5, 64x
С декоратором @profile все три задачи отрабатываются с одинаковым количеством использования памяти

Line #    Mem usage    Increment   Line Contents
================================================
    38     41.4 MiB     41.4 MiB   @profile
    39                             def sights():
    40     41.4 MiB      0.0 MiB       str_lst = string.printable
    41     41.4 MiB      0.0 MiB       lst = []
    42     41.4 MiB      0.0 MiB       p = 32
    43     41.4 MiB      0.0 MiB       w = 0
    44     41.4 MiB      0.0 MiB       for z in range(96):
    45     41.4 MiB      0.0 MiB           lst.append(p)
    46     41.4 MiB      0.0 MiB           p += 1
    47                             
    48     41.4 MiB      0.0 MiB       for x in lst:
    49     41.4 MiB      0.0 MiB           for c in range(1):
    50     41.4 MiB      0.0 MiB               print((chr(x) + ' - ' + str(x)), end = ' ')
    51     41.4 MiB      0.0 MiB               w += 1
    52     41.4 MiB      0.0 MiB               if w % 10 != 0:
    53     41.4 MiB      0.0 MiB                   continue
    54                                         else:
    55     41.4 MiB      0.0 MiB                   print('')

Проверила отдельные переменные в первых двух задачах с помощью show_sizeof, результат:

Первая задача:
show_sizeof(num) -  Тип: <class 'int'>, Размер: 16
show_sizeof(w) - Тип: <class 'int'>, Размер: 16
show_sizeof(num_choice) - Тип: <class 'int'>, Размер: 16

Вторая задача:
show_sizeof(str_lst) -  Тип: <class 'str'>, Размер: 128
show_sizeof(lst) - Тип: <class 'list'>, Размер: 2000
show_sizeof(p) - Тип: <class 'int'>, Размер: 16
show_sizeof(w) - Тип: <class 'int'>, Размер: 16

Судя по всему из-за создания списка перввая программа наиболее эффективно использует память.
Вероятно, если изменить код, чтобы значения из листа печатались сразу, не записываясь в список,
память использовалась бы более эффективно.
'''

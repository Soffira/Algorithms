""" Task 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков."""

import timeit
import random

#Один вариант
def example1():
    def lst_range():
        size_ = 100
        range_ = 10
        lst = [random.randint(-range_, range_) for _ in range(size_)]
        return lst

    def main():
        lst_r = lst_range()
        print("lst:", lst_r)
        num = max(lst_r, key=lst_r.count)
        print('Число', num, 'встречается', lst_r.count(num), 'раз')
    
# 2 Вариант
def example2():
    def get_key(d, value):
        c = []
        for k, v in d.items():
            if v == value:
                c.append(k)
        return c

    def main2():
        a = {}
        b = []

        for f in range(100):
            f = random.randint(-10, 10)
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
            print('в массиве {} встречается чаще всего.'.format(b))
        elif len(c) > 1:
            print('Числа', end = ' ')
            for x in c:
                print(str(x), end = ', ')
            print('в массиве {} встречается чаще всего.'.format(b))

print("Время выполнения первым методом: ", timeit.timeit("example1()", setup="from __main__ import example1", number=1))
print("Время выполнения вторым методом: ", timeit.timeit("example2()", setup="from __main__ import example2", number=1))

#Время выполнения задач практически одинаковое

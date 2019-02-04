'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)       
    lefthalf = merge_sort(lst[:middle])
    righthalf = merge_sort(lst[middle:])
    return merge(lefthalf, righthalf)

def merge(lefthalf, righthalf):
    result = []
    while len(lefthalf) > 0 and len(righthalf) > 0:
        if lefthalf[0] <= righthalf[0]:
            result.append(lefthalf[0])
            lefthalf = lefthalf[1:]
        else:
            result.append(righthalf[0])
            righthalf = righthalf[1:]
            
    if len(lefthalf) > 0:
        result += lefthalf
    elif len(righthalf) > 0:
        result += righthalf
    
    return result
    

mass = []
for f in range(10):
    f = round(random.uniform(0, 50), 2)
    mass.append(f)
    
print(mass)
mass_sort = merge_sort(mass)
print(mass_sort)
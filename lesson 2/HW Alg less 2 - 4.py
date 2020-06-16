""" Task 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры."""

lst = []
lst2 = []
x = 1
w = 1
t = 0
n = int(input('Введите количество элементов для расчета: '))
for c in range(n):
    lst.append(x)
    x = x/2
    
for s in lst:
    if n % 2 == 0:
        lst2.append(lst[t])
        s = lst[w]*-1
        lst2.append(s)    
        w += 2
        t += 2 
        if len(lst) >= w+1:
            continue
        else:
            break
    elif n % 2 != 0:
        lst2.append(lst[t])
        s = lst[w]*-1
        lst2.append(s)    
        w += 2
        t += 2         
        if len(lst) > w:
            continue
        else:
            lst2.append(lst[t])
            break
print(sum(lst2))

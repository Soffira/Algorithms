""" Task 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число."""

n = int(input('Введите любое натуральное число: '))

x = 1
decision = 0
lst = []
for x in range(n):
    x += 1
    lst.append(x)

for z in lst:
    decision += z

decision2 = (n*(n+1))/2

print(float(decision), float(decision2))
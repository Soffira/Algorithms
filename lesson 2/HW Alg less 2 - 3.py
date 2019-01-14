""" Task 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран."""

list_num = []

num = input('Введите число: ')
for char in reversed(num):  
    list_num.append(char)
print('"Обратное" число равно ' + ''.join(list_num))
""" Task 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число."""

import random

print('Отгадайте число за 10 попыток')
num = random.randint(0, 100)
w = 0
for x in range(10):
    num_choice = int(input('Введите число: '))
    if num_choice == num:
        print('Вы выиграли!')
        break
    elif num_choice > num:
        print('Неверно! Введенное Вами число больше, пропробуйте еще раз: ')
        w += 1
        if w == 10:
            print('Верное число = {}'.format(num))  
    elif num_choice < num:
        print('Неверно! Введенное Вами число меньше, пропробуйте еще раз: ')
        w += 1
        if w == 10:
            print('Верное число = {}'.format(num))    
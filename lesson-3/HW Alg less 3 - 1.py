""" Task 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9."""

a = []
b = [i for i in range(2,10)]
c = 0
 
for x in range(2,100):
    for y in b:
        if x % y != 0:
            continue
        else:
            a.append(x)
            break

print('{} чисел от 2 до 99 кратны любому из чисел в диапазоне от 2 до 9'.format(len(a)))
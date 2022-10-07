"""
Задача 8. НОД
Что нужно сделать

Напишите функцию, вычисляющую наибольший общий делитель двух чисел.
"""

def divisor(num_1, num_2):
    max_divisor = 0
    for n in range(1, num_1 + 1):
        if num_1 % n == 0 and num_2 % n == 0:
            max_divisor = n
    print('Максимальный делитель:', max_divisor)

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
divisor(number_1, number_2)






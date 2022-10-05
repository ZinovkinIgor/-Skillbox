"""
Задача 10. Яма
Что нужно сделать

Вы пишите компьютерную игру с текстовой графикой, вам поручили написать генератор ландшафта.
Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы» вот так:
"""

numbers = int(input('Введите число: '))
for row in range(1, numbers + 1):
    for col in range(numbers, 0, -1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    for col in range(1, numbers + 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    print()


print('=' * 20, 'ИЛИ', '=' * 20)
for row in range(numbers, 0, - 1):
    for col in range(numbers, 0, -1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    for col in range(1, numbers + 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    print()


print('=' * 20, 'ИЛИ', '=' * 20)
for row in range(numbers, 0, - 1):
    for col in range(1, numbers + 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    for col in range(numbers, 0, - 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    print()


print('=' * 20, 'ИЛИ', '=' * 20)
for row in range(1, numbers + 1):
    for col in range(1, numbers + 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    for col in range(numbers, 0, - 1):
        if row <= col:
            print(col, end='')
        else:
            print('.', end='')
    print()
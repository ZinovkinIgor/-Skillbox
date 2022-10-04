"""
Задача 4. Крест
Что нужно сделать

Напишите программу, которая выводит на экран крест из символов ^
(символы выводятся по диагоналям воображаемого квадрата).
"""

widch = int(input('Введите ширину рамки: '))
height = int(input('Введите высоту рамки: '))
for row in range(1, height + 1):
    for col in range(1, widch + 1):
        if row == col or row == - col + widch + 1:
            print('^', end='')
        else:
            print(' ', end='')
    print()

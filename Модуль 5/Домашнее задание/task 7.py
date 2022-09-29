"""
Задача 7. Костя хочет выигрывать
Что нужно сделать

После игры в кубики Костя захотел немного изучить работу игровых автоматов, а заодно математику и теорию вероятностей.
Но ему нужно с чего-то начать: написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.
Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).

Советы и рекомендации
По возможности уделите внимание сокращению кода и избегайте проверки условий, которые уже были проверены.
Если вы проверили условие condition, то не следует проверять not condition после.
"""

numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
numb3 = int(input('Введите третье число: '))
if numb1 == numb2 == numb3:
    print('3 числа совпадают.')
elif numb1 == numb2 or numb1 == numb3 or numb2 == numb3:
    print('2 числа совпадают.')
else:
    print('0 все числа разные.')



"""
Задача 1. Врата
Напишите программу, которая выводит в консоль «врата», состоящие из тире, вертикальных линий и пробелов.
Поле состоит из 20 строк и 30 столбцов (но не стесняйтесь пробовать и другие размеры).

Задача 2. Дорога
Мы делаем текстовую игру — гонку, и нам нужно вывести на экран что-то вроде трассы, где будут соревноваться наши машины.
Напишите программу, которая выводит такую дорогу на экран (поле 20×50).

Что нужно сделать, чтобы обочины рисовались поверх горизонтальной линии?

Задача 3. Диагональная матрица
Напишите программу, которая получает на вход размер квадратной матрицы и выводит на экран по такому принципу диагональ
из единиц с левого нижнего угла до верхнего правого, ниже диагонали — двойки, выше — нули.
Пример:
"""

# Задача 1
print('=' * 40)
print('Задача 1')
for row in range(1, 21):
    for col in range(1, 51):
        if row == 1:
            print('_', end='')
        elif col == 1 or col == 50:
            print('|', end='')
        else:
            print(' ', end='')
    print()

# Задача 2
print('=' * 40)
print('Задача 2')
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end='')
        elif col == row + 30:
            print('\\', end='')
        elif col == 25:
            print('|', end='')
        elif col == -row + 20:
            print('/', end='')
        else:
            print(' ', end='')
    print()

# Задача 3
print('=' * 40)
print('Задача 3')
number = int(input('Введите число: '))
for row in range(1, number + 1):
    for col in range(number, 0, -1):
        if row < col:
            print('0', end='\t')
        elif row > col:
            print('2', end='\t')
        else:
            print('1', end='\t')
    print()


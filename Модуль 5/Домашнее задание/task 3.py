"""
Задача 3. Функция
Что нужно сделать

Учитель математики придумывает каждому своему ученику отдельные функции, которые нужно отобразить на графике и посчитать.
А ещё этот учитель разбирается в программировании. Поэтому, чтобы не считать вручную все эти функции, он написал программу,
которая делает всю работу за него.
Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:
y= {x −12, x>0, 5,  x=0 x²,  x<0
Напомним, как это работает:
для X > 0, Y = X − 12
для X = 0,  Y = 5
для X < 0, Y = X²

Пример:
Введите икс: 0
Игрек равен 5

Пример 2:
Введите икс: −6
Игрек равен 36

Советы и рекомендации
По возможности уделите внимание сокращению кода и избегайте проверять условия, которые уже были проверены.
Если вы проверили условие condition, то не следует проверять not condition после.
"""

x = int(input('Введите икс: '))
if x > 0 or x < 0:
    if x > 0:
        y = x - 12
        print('Игрек равен:', y)
    else:
        y = x ** 2
        print('Игрек равен:', y)
else:
    y = 5
    print('Игрек равен:', y)
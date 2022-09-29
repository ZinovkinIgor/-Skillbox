"""
Задача 1. Калькулятор опыта
Что нужно сделать

Андрей любит играть в компьютерные игры. В один прекрасный день у него появилась классная идея для сюжета своей игры.
Чтобы воплотить её в жизнь, он начал изучать программирование и геймдизайн. Начал он с главного героя и его системы прокачки.
Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков опыта»,
а программа вычисляет уровень. Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.

Пример:
Введите количество опыта: 6000
Ваш уровень: 4

Пример 2:
Введите количество опыта: 2000
Ваш уровень: 2

Советы и рекомендации
По возможности уделите внимание сокращению кода и избегайте проверять условия, которые уже были проверены.
Если вы проверили условие condition, то не следует проверять not condition после.
"""

experience = int(input('Введите количество опыта: '))
if experience >= 1000 and experience < 2500:
    level = 2
elif experience >= 2500 and experience < 5000:
    level = 3
elif experience >= 5000:
    level = 4
else:
    level = 1
print('Ваш уровень:', level)
"""
Задача 1. Вода
Одна бутылка воды «КлирВотер» от производителя «ВодЗавод» в разных магазинах стоит по-разному.
Напишите программу, которая три раза вызывает функцию aboutWater, передаёт в неё один аргумент —
цену на воду и выводит на экран название воды, производителя и цену.

Пример:
Название: КлирВотер
Производитель: ВодЗавод
Цена: 25

Название: КлирВотер
Производитель: ВодЗавод
Цена: 30

Название: КлирВотер
Производитель: ВодЗавод
Цена: 40

Задача 2. Вот это объёмы 2
Андрей продолжает писать курсовую работу по физике, и теперь ему нужно находить не только объём планеты,
но и её площадь. Для этого он использует две такие формулы:
Формула для площади сферы:
Формула для объёма шара:

Так как в самом курсовом проекте эти формулы пригодятся ещё не раз, Андрей решил поступить рационально и
просто написать функцию для каждой формулы.
Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число) и вызывает
функции sphereArea и sphereVolume. Реализуйте эти функции: первая считает и выводит на экран площадь сферы, вторая — объём шара.

Задача 3. Простые числа
Пользователь вводит число N — количество чисел в последовательности. Напишите программу, которая проверяет,
сколько из этих чисел являются простыми. Для проверки простоты числа реализуйте функцию isPrime.
"""


# Задача 1
print('=' * 40)
print('Задача 1')

def aboutWater(price):
    print('Название: КлирВотер')
    print('Производитель: ВодЗавод')
    print('Цена:', price)
    print('\n')

aboutWater(25)
aboutWater(30)
aboutWater(35)

# Задача 2
print('=' * 40)
print('Задача 2')
import math
def sphereArea(r):
    s = 4 * math.pi * r ** 2
    print('Площадь сферы:', s)
def sphereVolume(r):
    v = (4 / 3) * math.pi * r ** 3
    print('Объём шара', v)

planet = float(input('Введите радиус планеты: '))
sphereArea(planet)
sphereVolume(planet)


# Задача 3
print('=' * 40)
print('Задача 3')

def isPrime(numb):
    for row in range(2, numb + 1):
        for col in range(2, row):
            if row % col == 0:
                break
        else:
            print(row)

numbers = int(input('Введите число: '))
isPrime(numbers)
"""
Задача 1. Создание кортежей
Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж числами от −5 до 0.
Объедините два кортежа, создав тем самым третий кортеж. С помощью метода кортежа определите в нём количество нулей.
Выведите на экран третий кортеж и количество нулей в нём.

Задача 2. Цилиндр
Андрей однажды уже писал функции для расчёта площади сферы и объёма шара. И теперь для своей курсовой работы ему пришлось
связаться с цилиндрами.
Пользователь вводит два значения: радиус и высоту. Напишите функцию для расчёта площади боковой поверхности цилиндра и
его полной площади. Функция должна возвращать два эти значения. После этого в основной программе выводятся оба ответа в две строки.
Площадь боковой поверхности (r — радиус, h — высота):
Полная площадь (S — площадь круга):

Задача 3. Неправильный код
Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел. Затем вызывается функция,
которая получает на вход кортеж чисел, генерирует случайный индекс и случайное значение, а затем по этим индексу и
значению меняет сам кортеж. Функция должна возвращать кортеж и случайное значение.
В основном коде функция используется два раза, и на экран два раза выводится новый кортеж и случайное значение.
Причём второй раз выводится сумма первого случайного значения и второго.
Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.

import random

def change(nums):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value

my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums = change(new_nums)
rand_val += change(new_nums)
print(new_nums, rand_val)
"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    import random
    number_tuple_1 = tuple(random.randint(0, 5) for _ in range(10))
    number_tuple_2 = tuple(random.randint(-5, 0) for _ in range(10))
    tuple_3 = tuple(number_tuple_1 + number_tuple_2)
    print('Весь кортеж', tuple_3)
    print('Количество 0:', tuple_3.count(0))

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    import math

    def formula(r, h):
        side = 2 * math.pi * r * h
        s = math.pi * r ** 2
        full = side + 2 * s
        return side, full


    radius = int(input('Введите радиус: '))
    hight = int(input('введите высоту: '))
    result = formula(radius, hight)
    print('Площадь боковой поверхности: ', result[0])
    print('Полная площадь: ', result[1])


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    import random


    def change(nums):
        index = random.randint(0, 5)
        value = random.randint(100, 1000)
        num_list = list(nums)
        num_list[index] = value
        nums = tuple(num_list)

        return nums, value


    my_nums = 1, 2, 3, 4, 5

    new_nums, rand_val = change(my_nums)
    print(new_nums, rand_val)
    new_nums, new_rond = change(new_nums)
    rand_val += new_rond
    print(new_nums, rand_val)

else:
    print('Выберите задачу заново.')



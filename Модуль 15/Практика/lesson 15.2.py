"""
Задача 1. Гугл
Программисты постоянно гуглят ошибки и ищут уже готовый код, который можно использовать для своей программы,
чтобы не изобретать велосипед. Андрей поступил также и нашёл для своего проекта код, который должен находить
минимальное и максимальное числа в списке. Вот этот код:
nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
 num = int(input('Очередное число: '))
 nums_list.append(num)
maximum = 0
minimum = -1
for i in nums_list:
 if maximum < i:
   maximum = i
 if minimum > i:
   minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)
Однако он столкнулся с проблемой. Если брать, к примеру, количество чисел 5, то на тестах -1 -2 -3 -4 -5 и 1 2 3 4 5
программа выводит неверный результат.
Доработайте программу так, чтобы она выводила верный результат. Подсказка: для отладки используйте точки останова.

Задача 2. Кратность
Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов списка,
которые кратны K.

Пример:
Кол-во чисел в списке: 4
Введите 1 число: 1
Введите 2 число: 20
Введите 3 число: 30
Введите 4 число: 4

Введите делитель: 10

Индекс числа 20: 1
Индекс числа 30: 2
Сумма индексов: 3

Задача 3. Собачьи бега
В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. На огромном табло
выводятся очки каждой собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим количеством очков
поменялись местами! Нужно это исправить.
Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.
"""


# Задача 1
print('=' * 40)
print('Задача 1')
nums_list = []
N = int(input('Кол-во чисел в списке: '))
for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)
maximum = nums_list[0]
minimum = nums_list[0]
for i in nums_list:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
print('Максимальное число в списке:', maximum)
print('Минимальное число в списке:', minimum)


# Задача 2
print('=' * 40)
print('Задача 2')

count_number = int(input('Введите количество чисел: '))
numbers = []
sum_index = 0
for scor in range(count_number):
    print('Введите', scor + 1,'число: ', end='')
    new_numb = int(input())
    numbers.append(new_numb)
devisor = int(input('\nВведите делитель: '))

for index in range(count_number):
    if numbers[index] % 10 == 0:
        print('Индекс числа', numbers[index], ':', index)
        sum_index += index
print('\nСумма индексов:', sum_index)


# Задача 3
print('=' * 40)
print('Задача 3')

dog = int(input('Введите количество собак: '))
ball_dog = []

for scor in range(dog):
    print('Сколько баллов получила', scor, 'собака: ', end='')
    ball = int(input())
    ball_dog.append(ball)

print(ball_dog)
ball_min, ball_max, i_min, i_max = ball_dog[0], ball_dog[0], 0, 0

for col in range(dog):
    if ball_dog[col] > ball_max:
        ball_max = ball_dog[col]
        i_max = ball_dog.index(ball_max)
    elif ball_dog[col] < ball_min:
        ball_min = ball_dog[col]
        i_min = ball_dog.index(ball_min)

ball_dog[i_min], ball_dog[i_max] = ball_dog[i_max], ball_dog[i_min]
print(ball_dog)



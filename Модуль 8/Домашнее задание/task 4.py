"""
Задача 4. Среднее на отрезке
Что нужно сделать

Напишите программу, которая считывает с клавиатуры числа a, b и c, считает и выводит на консоль
среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.
"""

num_beginning = int(input('Введите первое число: '))
num_end = int(input('Введите второе число: '))
num_divider = int(input('Введите третье число: '))
sum_num, score = 0, 0
for number in range(num_beginning, num_end + 1):
    if number % num_divider == 0:
        sum_num += number
        score += 1
print('Среднее арифметическое число:', sum_num / score)

"""
Задача 10. За что?
Что нужно сделать

Вы встретились со своим старым другом, который тоже изучает программирование, правда, в другом учебном заведении.
За чашкой кофе он пожаловался вам, что сумасбродный препод дал им задание написать программу, которая из двух
введённых чисел определяет наибольшее, не используя при этом условных операторов, циклов и встроенную функцию max.
Радуясь, что на вашем курсе такого не требуют, вы всё-таки решаете помочь своему другу. Напишите для него эту программу.

Пример:
Введите первое число: 10
Введите второе число: 5
Наибольшее число: 10
"""

numb_1 = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))
result = ((numb_1 + numb_2) / 2) + (abs(numb_1 - numb_2) / 2)
print('Наибольшее число: ', int(result))





"""
Задача 6. Сумма факториалов
Что нужно сделать

Напишите программу, которая запрашивает у пользователя число N и находит сумму факториалов 1! + 2! + 3! + ... + n!
"""

numbers = int(input('Введите число: '))
sum_fact = 0
for row in range(1, numbers + 1):
    summ = 1
    for col in range(1, row + 1):
        summ *= col
    print('Сумма от', row,'факториала', summ)
    sum_fact += summ
print('Сумма факториалов: ', sum_fact)
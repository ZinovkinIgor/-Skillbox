"""
Задача 8. Колонтитул
Что нужно сделать

Нам нужно написать программу для печати важных объявлений. Сверху объявления должен располагаться вот такой колонтитул:
Восклицательные знаки всегда располагаются по центру строки, причём в зависимости от важности объявления
количество восклицательных знаков может быть разным. Напишите программу, которая спрашивает у пользователя
сначала общую длину колонтитула в символах, потом желаемое количество восклицательных знаков,
после чего выводит на экран готовую строку.
"""

long = int(input('Введите длину колонтитула: '))
sign_numbers = int(input('Введите сколько восклицательных знаков: '))
num = (long - sign_numbers) // 2
print(('~' * num) + ('!' * sign_numbers) + ('~' * num))


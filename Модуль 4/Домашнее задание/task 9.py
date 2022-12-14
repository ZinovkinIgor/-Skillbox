"""
Задача 9. Плохой циферблат
Что нужно сделать

У Саши в грузовике стоит суперсовременный цифровой циферблат для подсчёта пробега, но он постоянно
 сбрасывается. Саша заметил закономерность: каждый раз, когда сумма цифр пробега на циферблате
 превышает число текущего дня, циферблат сбрасывается.
Напишите программу, которая получает на вход от пользователя два числа: трёхзначное число пробега
 и число дня, затем находит сумму цифр первого числа и, если эта сумма больше числа дня, выводит
 сообщение «Сброс» и сбрасывает пробег до нуля. В противном случае выводится: «Сегодня не сломался».
 В конце также выводится сам пробег.

Пример 1:
Введите пробег: 123
Введите сегодняшнее число: 5
Сброс.
Пробег: 0

Пример 2:
Введите пробег: 123
Введите сегодняшнее число: 10
Сегодня не сломался.
Пробег: 123
"""
mileage = int(input('Введите пробег: '))
day = int(input('Введите сегодняшнее число: '))

num1 = mileage // 100
num2 = mileage % 100 // 10
num3 = mileage % 10
summ = num1 + num2 + num3
if summ >= day:
    print('Сброс.')
else:
    print('Пробег:', mileage)
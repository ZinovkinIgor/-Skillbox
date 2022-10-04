"""
Задача 7. Наибольшая сумма цифр
Что нужно сделать

Пользователь вводит N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
Выведите на экран это число и сумму его цифр.
"""

counter = int(input('Введите количество чисел: '))
sum_number, numb = 0, 0
for _ in range(counter):
    summ = 0
    numbers = int(input('Введите число: '))
    nom = numbers
    while numbers > 0:
        summ += numbers % 10
        if summ > sum_number:
            sum_number = summ
            numb = nom
        numbers //= 10
print('Максимальное число', numb, 'его сумма', sum_number)
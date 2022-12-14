"""
Задача 1. Сумма чисел 2
Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму
всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

Пример работы программы:
Введите число: 5
Сумма от 1 до 5 = 15
Сумма от 1 до 15 = 120

Задача 2. «Назад в будущее»
Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль, который можно
было бы просто подключить внутри программы и облегчить жизнь всем программистам.
Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих двух чисел.

Пример работы программы:
Введите первое число: 6
Введите второе число: 10
НОД = 2

Задача 3. Приоритет задач
В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, а затем уже идут небольшие.
Каждая из этих задач, по сути, просто огромный поток цифр. Ваша задача, как программиста этого центра, написать программу,
которая поможет определять, какую из задач нужно решать в первую очередь.
Вводится последовательность из N чисел. Нужно определить номер числа, у которого больше всего цифр, и вывести на экран
соответствующее сообщение. Если число отрицательное, то считать его за 0. Для подсчёта количества цифр реализуйте функцию numeral_count.

Пример работы программы:
Введите кол-во задач: 4
Введите число: 6
Введите число: 14
Введите число: 1
Введите число: 13434
Первая задача на обработку: 13434
"""

# Задача 1
print('=' * 40)
print('Задача 1')

def summa_n(nnum):
    summ = 0
    for n in range(1, nnum + 1):
        summ += n
    print('Сумма от 1 до', nnum, '=', summ)
    return summ

numbers = int(input('Введите число: '))
new_summa_n = summa_n(numbers)
summa_n(new_summa_n)

# Задача 2
print('=' * 40)
print('Задача 2')

def max_divisor(a, b):
    divisor = 0
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a

    return a + b

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
max_div = (max_divisor(number_1, number_2))
print('Максимальный делитель: ', max_div)

# Задача 3
print('=' * 40)
print('Задача 3')

def bigTask(n):
    count = 0
    while n > 0:
        count += 1
        n = n / 10
    return count



score = int(input('Введите кол-во задач: '))
task, max_num = 0, 0
for num in range(1, score + 1):
    number = int(input('Введите число: '))
    new_task = bigTask(number)
    if new_task > task:
        max_num = number
        task = new_task
print('Первая задача на обработку:', max_num)




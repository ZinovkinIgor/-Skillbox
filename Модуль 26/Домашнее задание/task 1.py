"""
Задача 1. Квадраты чисел
Что нужно сделать

Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N
(1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами: класс-итератор,
функция-генератор и генераторное выражение.
"""

task = int(input('Выберите какую задачу выполнить (1-класс-итератор, 2-функция-генератор, 3-генераторное выражение) '))

if task == 1:
    # Задача 1
    print('=' * 40)
    print('1-класс-итератор')

    class Square:
        def __init__(self, number):
            self.number = number
            self.score = 0

        def __iter__(self):
            return self

        def __next__(self):
            while self.score < self.number:
                self.score += 1
                yield self.score ** 2

    numb = Square(5000000)
    for n in numb.__next__():
        print(n)

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('2-функция-генератор')

    def func_square(number):
        i = 0
        while i <= number:
            yield i ** 2
            i += 1


    numb = func_square(5)
    for n in numb:
        print(n)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('3-генераторное выражение')

    square_number = (x ** 2 for x in range(1, 11))
    for n in square_number:
        print(n)


else:
    print('Выберите задачу заново.')
"""
Задача 1. Простая программа
Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
Используйте операторы try except else finally. Обработайте возможные ошибки:
Проблема при открытии файла.
Нельзя преобразовать данные в целое.
Неожиданная ошибка.

Задача 2. Старая задача
Возьмите любую задачу из домашнего задания, например, предыдущего модуля и оформите её решение в
виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос: когда стоит использовать
обработку исключений и когда она будет излишней?
"""
import os
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    try:
        text = open('new_text.txt', 'r')
    except FileNotFoundError:
        print('Такого файла не существует.')
    try:
        numbers = int('d')
        print(numbers)
    except ValueError:
        print('Нельзя преобразовать данные в целое.')
    try:
        numb = 99 / 2
        print(numb)
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    finally:
        print('Завершаем работу')




elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    """
    try except finally лучше использовать когда ввод идет от пользователя, можно заменить множество проверок if elif
    """

    adress_project = os.path.abspath(os.path.join('..'))
    for i_path, i_dept, i_file in os.walk(adress_project):
        print(i_dept)
    print(adress_project)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
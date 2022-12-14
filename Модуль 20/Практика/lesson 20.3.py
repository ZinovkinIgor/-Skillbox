"""
Задача 1. Саботаж!
Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил в код сайта символ ~ (тильда).
Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль индексы символа ~.
Для решения этой задачи (и остальных тоже) используйте функцию enumerate.

Пример:
Строка: so~mec~od~e
Ответ: 2 6 9

Задача 2. Словари из списков
Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться). Затем для каждого
списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
Подсказка: random

Пример:
Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}

Задача 3. Универсальная программа
Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд. При этом он заранее предупредил,
что скрипт должен уметь работать с любым итерируемым типом данных.
Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
у которых индекс чётный.

Пример 1:
Допустим, есть такая строка: 'О Дивный Новый мир!'
Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']

Пример 2:
Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
Результат: [100, 300, 0, 'а']

Примечание: для проверки типа можно использовать функцию
isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных,
и возвращает False в противном случае.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)
    string = input('Строка: ')
    print('Ответ: ', end='')
    for index, simbol in enumerate(string):
        if simbol == '~':
            print(index, end=' ')

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    import random
    import string

    def formula(new_list, new_dict):
        for index, simbol in enumerate(new_list):
            new_dict[index] = simbol
        return new_dict

    dict_1 = dict()
    dict_2 = dict()
    list_1 = [random.choice(string.ascii_lowercase) for _ in range(10)]
    list_2 = [random.choice(string.ascii_lowercase) for _ in range(10)]
    print('Первый словарь:', formula(list_1, dict_1))
    print('Второй словарь:', formula(list_2, dict_2))

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


    def processing(i):
        for index, simbol in enumerate(i):
            if index % 2 != 0:
                new_line.append(simbol)
        return new_line

    a = 'О Дивный Новый мир!'
    b = [100, 200, 300, 'буква', 0, 2, 'а']
    c = (3, 'Hello', [9, 8, 00], 9.87)
    d = {'one': 1, 'two': 2, 'free': 3}
    new_line = []
    for i in a, b, c, d:
        if isinstance(i, str):
            print('Допустим есть такая строка: ', i)
            new_line = processing(i)
        elif isinstance(i, list):
            print('Допустим есть такая список: ', i)
            new_line = processing(i)
        elif isinstance(i, dict):
            print('Допустим есть такая словарь: ', i)
            new_line = processing(i)
        elif isinstance(i, tuple):
            print('Допустим есть такая картеж: ', i)
            new_line = processing(i)
    print('Результат: ', new_line)


else:
    print('Выберите задачу заново.')



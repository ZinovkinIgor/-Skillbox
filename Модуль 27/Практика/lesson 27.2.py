"""
Задача 1. Функции
Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:

def func_1(x):
    return x + 10

Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
Пример основного кода:
print(func_2(func_1, 9))

Результат: 361.


Задача 2. Таймер
Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость передачи
данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время вам было лень,
поэтому возникла идея написать «автотест», который всё сделает сам.
С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы
переданной функции func и выдаёт ответ на экран.
Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.
"""

import os
import time
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    def func_1(x) -> int:
        """Функция возвращает число увеличенное на 10"""
        return x + 10

    def func_2(numb, *args, **kwargs) -> int:
        """Функция получает функцию и перемножает их, подает на вывод сумму чисел"""
        return numb(*args, **kwargs) * numb(*args, **kwargs)

    numbers = int(input('Введите число: '))
    print(func_1(numbers))
    print(func_2(func_1, numbers))



elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')



    '''
    1 - находим файл .py
    2 - открываем файл и считаем строки все кроме комментариев и пустых 
    3 - общее количество выводим на экран
    '''


    def search_file(directory: str) -> str:
        summ_lines = 0
        summ_comment = 0
        summ_not_simbol = 0
        summ_simbol = 0
        '''
        :param directory: откуда идет поиск 
        :return: общее количество строк во всех файлах
        '''

        for root, direct, files in os.walk(directory):
            """
            Открываем директорию и проходим по файлам если файл с разрешением .py, то открываем его
            иначе пропускаем, если это каталог, то заходим в каталог и ищем в нем.
            """
            for file in files:
                if file.endswith('.py'):
                    text_file = '\\'.join([root, file])
                    with open(text_file, 'r', encoding='utf-8') as text:
                        """
                        открыли питоновский файл, проходим по каждой строчке, проверяем на комментарии и пустые строчки
                        """
                        res = text.read()
                        count_string = 0
                        count_comment = 0
                        not_simbol = 0
                        count_simbol = 0
                        for string in res.split('\n'):
                            count_string += 1
                            if string.startswith('#'):
                                print('Комментарий в строке {string}. Адрес: {adress}'.format(
                                    string=count_string, adress='\\'.join([root, file])
                                ))
                                count_comment += 1
                            elif string == '':
                                print('Пустая строка {string}. Адрес: {adress}'.format(
                                    string=count_string, adress='\\'.join([root, file])
                                ))
                                not_simbol += 1
                            else:
                                count_simbol += 1
                        print('Комментариев {}'.format(count_comment))
                        print('Пустых строк {}'.format(not_simbol))
                        summ_comment += count_comment
                        summ_not_simbol += not_simbol
                        summ_lines += count_string
                        summ_simbol += count_simbol

        return summ_lines, summ_comment, summ_not_simbol, summ_simbol


    directory = os.path.abspath(os.path.join('..', '..'))
    start_func = time.time()
    number_of_rows = search_file(directory)
    print(
        'Количество строк в документе: {string}.\nКоличество заполненных строк: {simb}\nКомментарии: {comment}\nПустые строки: {clear}'.format(
            string=number_of_rows[0],
            comment=number_of_rows[1],
            clear=number_of_rows[2],
            simb=number_of_rows[3]))
    end_func = time.time()
    result = round(end_func - start_func, 4)
    print('Время выполнения функции: {} сек.'.format(result))


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')


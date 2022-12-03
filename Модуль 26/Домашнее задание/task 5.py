"""
Задача 5. Количество строк
Что нужно сделать

Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет общее количество строк кода,
игнорируя пустые строки и строчки комментариев.
"""

import os
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
number_of_rows = search_file(directory)
print('Количество строк в документе: {string}.\nКоличество заполненных строк: {simb}\nКомментарии: {comment}\nПустые строки: {clear}'.format(
    string=number_of_rows[0],
    comment=number_of_rows[1],
    clear=number_of_rows[2],
    simb=number_of_rows[3]))
print()
#
# Задача 1. Сисадмин
# Вы работаете системным администратором в одной компании. На диске каждого сотрудника компании в специальной папке
# access лежит файл admin.bat. Этот файл предназначен для вас, и вам нужен путь до этого файла, причём как относительный,
# так и абсолютный. Недолго думая, вы решили написать небольшой скрипт, который закинете по сети к этому файлу.
# Напишите программу, которая выводит на экран относительный и абсолютный пути до файла admin.bat.
#
# Пример результата:
# Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
#
# Относительный путь до файла: Skillbox\access\admin.bat
#
# Задача 2. Содержимое
# Выберите любую директорию на своём диске и затем напишите программу, выводящую на экран абсолютные пути к файлам и папкам,
# которые находятся внутри этой директории.
#
# Результат программы на примере директории проекта python_basic:
# Содержимое каталога G:\PycharmProjects\python_basic
#     G:\PycharmProjects\python_basic\.git
#     G:\PycharmProjects\python_basic\.idea
#     G:\PycharmProjects\python_basic\Module14
#     G:\PycharmProjects\python_basic\Module15
#     G:\PycharmProjects\python_basic\Module16
#     G:\PycharmProjects\python_basic\Module17
#     G:\PycharmProjects\python_basic\Module18
#     G:\PycharmProjects\python_basic\Module19
#     G:\PycharmProjects\python_basic\Module20
#     G:\PycharmProjects\python_basic\Module21
#     G:\PycharmProjects\python_basic\Module22
#
# Задача 3. Корень диска
# Напишите программу, которая выводит на экран только корень диска, на котором запущен скрипт.
# Учтите, что скрипт может быть запущен где угодно и при любой вложенности папок.
#
# Результат программы на примере диска G:
# Корень диска: G:\\
#

import os.path

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    adress = os.path.abspath('admin.bat')
    print(adress)
    adress_2 = os.path.abspath(os.path.join('..', '..', 'admin.bat'))
    print(adress_2)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    def print_search_path(path):
        print('Проверяем директорию {}'.format(path))
        for name in os.listdir(path):
            print(os.path.join(path, name))

    search = ['Домашнее задание', 'Практика']
    for name in search:
        search_path = os.path.abspath(os.path.join('..',  name))
        print_search_path(search_path)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    result_9 = os.path.abspath(os.path.sep)
    print(result_9)


else:
    print('Выберите задачу заново.')

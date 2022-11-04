# """
# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска:
# папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение. Если путь указывает на файл,
# то также выведите его размер (сколько он весит в байтах). Обеспечьте контроль ввода: проверка пути на существование.
#
# Подсказка: для вывода размера файла поищите соответствующий метод.
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует
#
# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории. Однако,
# как мы понимаем, файлов с таким названием может быть несколько.
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, проходит по всем вложенным
# файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
#
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py
# """
import os

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    def print_dirc(project, key):
        print('переходим {}'.format(project))

        if os.path.exists(project):
            for name in os.listdir(project):
                patch = os.path.join(project, name)
                print('смотрим {}'.format(patch))
                if os.path.isfile(patch):
                    print('Абсолютный путь к файлу: {}'.format(patch))
                    print('Размер файла: {} байт'.format(os.stat(patch).st_size))
                    break
                if os.path.isdir(patch):
                    print('это директория: ')
                    result = print_dirc(patch, key)
                    if result:
                        break
        else:
            print('Такой директории нет.')

    search = ['lesson 22.2.py']
    for simb in search:
        path_dirc = os.path.abspath(os.path.join('..', '..', '..'))
        result = print_dirc(path_dirc, simb)



elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    adress_project = os.path.abspath(os.path.join('..', '..'))
    for i_path, i_dept, i_file in os.walk(adress_project):
        print(i_dept)
    print(adress_project)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')





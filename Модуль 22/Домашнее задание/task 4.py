"""
Задача 4. Файлы и папки
Что нужно сделать

Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска)
и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).
Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов.
Результат работы программы на примере python_basic\Module14:
E:\PycharmProjects\python_basic\Module14
Размер каталога (в Кб): 8.373046875
Количество подкаталогов: 7
Количество файлов: 15
"""

import os

def project_folder(adress, name, scor_files, scor_folder, summ):

    for i_name in os.listdir(adress):
        adr_2 = os.path.join(adress, i_name)
        if os.path.isdir(adr_2):
            scor_folder += 1
            res = project_folder(adr_2, name, scor_files, scor_folder, summ)
            scor_files = res[0]
            scor_folder = res[1]
            summ += res[2]
        elif os.path.isfile(adr_2):
            scor_files += 1
            summ += os.stat(adr_2).st_size

    return scor_files, scor_folder, summ


"""
Проходим по каталогу и ищем подходящий каталог.
Найденный каталог открываем и начинаем считать файлы и каталоги
"""
def search_files(adress, name):
    for i_name in os.listdir(adress):
        adr_1 = os.path.join(adress, i_name)
        if i_name == name:

            scor_files, scor_folder, summ = 0, 0, 0
            result = project_folder(adr_1, name, scor_files, scor_folder, summ)
            print('Адрес: {}'.format(adr_1))
            print('Размер каталога (в Кб): {}'.format(result[2]))
            print('Количество подкаталогов: {}'.format(result[1]))
            print('Количество файлов: {}'.format(result[0]))
            break


name = 'Модуль 21'

adress = os.path.abspath(os.path.join('..', '..'))
search_files(adress, name)




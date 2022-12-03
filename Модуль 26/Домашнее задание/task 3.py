"""
Задача 3. Пути файлов
Что нужно сделать

Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории
(по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
Решение задачи должно быть без рекурсии.

Подсказка:
Существует функция, которая может получать все имена файлов в дереве каталогов. Попробуйте найти ее самостоятельно.

"""

import os

def print_search(adress, directory, search_files):
    new_adress = os.path.abspath(os.path.join(os.path.sep, adress, directory))
    for adr, direct, files in os.walk(new_adress):
        print('\nАдрес: {}'.format(adr))
        for files_adr in files:
            print('\t\tФайл: ', os.path.abspath(os.path.join(os.path.sep, new_adress, files_adr)))
        for direct_adr in direct:
            print('\n\tПапка: ', os.path.abspath(os.path.join(os.path.sep, direct_adr)))
            print_search(adress=new_adress, directory=direct_adr, search_files=search_files)

def gen_files_path(adress, directory, search_files):
    new_adress = os.path.abspath(os.path.join(os.path.sep, adress, directory))
    for adr, direct, files in os.walk(new_adress):
        for direct_adr in direct:
            if direct_adr.lower().startswith(search_files.lower()):
                print_search(adress=new_adress, directory=direct_adr, search_files=search_files)
                print('+' * 77)
                break
            gen_files_path(adress=new_adress, directory=direct_adr, search_files=search_files)



adress = os.path.abspath(os.path.join(os.path.sep, 'Users', 'User', 'OneDrive', 'Рабочий стол'))
searth = input('введите каталог для поиска')
res = gen_files_path(adress=adress, directory='', search_files=searth)



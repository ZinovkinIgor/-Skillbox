"""
Задача 1. Работа с файлом 2
Что нужно сделать
Реализуйте модернизированную версию контекст-менеджера File:

теперь при попытке открыть несуществующий файл менеджер должен автоматически создавать и открывать этот файл в режиме записи;
на выходе из менеджера должны подавляться все исключения, связанные с файлами.
"""

from abc import ABC

class File(ABC):
    '''Класс файл: получает на вход документ который необходимо открыть и какой режим'''
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        '''открываем файл и возвращаем его'''
        self.file = open(self.filename, self.mode, encoding='utf-8') # Сюда добавил режим чтения
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        '''Закрываем файл и подавляются все исключения'''
        self.file.close()
        return True


name_file = input('Введите имя файла .txt: ')
with File(f'{name_file}.txt', 'w') as file:
    file.write('Всем привет')




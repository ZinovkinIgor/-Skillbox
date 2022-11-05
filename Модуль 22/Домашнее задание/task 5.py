"""
Задача 5. Сохранение
Что нужно сделать

Мы продолжаем работать над усовершенствованием своего текстового редактора. Конечно же, при работе с редактором
пользователь, скорее всего, захочет сохранить то, что он написал, в отдельный файл. Ну или перезаписать тот, в
котором он продолжил работать.
Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, куда он хочет сохранить
эту строку: вводится последовательность папок и имя файла (расширение .txt). Затем в этот файл сохраняется значение
переменной text. Если этот файл уже существует, то нужно спросить у пользователя, действительно ли он хочет перезаписать его.
Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.

Пример 1
Введите строку: programm test

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Файл успешно сохранён!

Содержимое файла:
programm test

Пример 2
Введите строку: testiruyem

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Вы действительно хотите перезаписать файл? да
Файл успешно перезаписан!

Содержимое файла:
testiruyem
"""

import os

def save_file(path, text, name_file, action):
    adress = os.path.join(path, '{}.txt'.format(name_file))
    projects = open(adress, action, encoding='utf-8')
    projects.write(text)
    projects.close()


def main():
    text = input('Введите строку: ')
    adress = input('\nКуда хотите сохранить документ? Введите последовательность папок (через запятую):\n').split(', ')
    name_file = input('Введите имя файла: ')
    path = os.path.abspath(os.path.sep)
    for name in adress:
        path = os.path.join(path, name)

    while True:
        if os.path.exists('{}.txt'.format(name_file)):
            answer = input('Вы действительно хотите перезаписать файл? ').lower()
            if answer == 'да':
                save_file(path, text, name_file, action='w')
                print('Файл перезаписан.')
                break
            elif answer == 'нет':
                save_file(path, text, name_file, action='a')
                print('Файл добавлен.')
                break
            else:
                print('Введите да или нет.')
        else:
            save_file(path, text, name_file, action='w')
            print('Файл сохранен.')
            break


main()



# Users, User, OneDrive, Рабочий стол, Bot, Восстанавливаем обучение Python, Модуль 22, Домашнее задание







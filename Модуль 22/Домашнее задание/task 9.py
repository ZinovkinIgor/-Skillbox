"""
Задача 9. Война и мир (необязательная)
Что нужно сделать
Мало кто не знает про знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит
в архиве voina-i-mir.zip. Напишите программу, которая подсчитает статистику по буквам (не только русского алфавита)
в этом романе и выведет результат на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости
букв (по возрастанию или убыванию). Регистр символов имеет значение.
Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива «вручную».
"""

import zipfile

def scor_simbol(name, text_analysis):
    '''
     Счетчик на повторение символов
    '''
    text = open(name, 'r', encoding='utf-8')
    for line in text:
        for simbol in line:
            if simbol in text_analysis:
                text_analysis[simbol] += 1
            else:
                text_analysis[simbol] = 1
    text.close()

# Распаковываем рахив, запускаем функцию
text_analysis = dict()
new_dict = dict()
text_zip = zipfile.ZipFile('voyna-i-mir.zip')
text_zip.extractall()

name = 'voyna-i-mir.txt'
text_zip.close()

scor_simbol(name, text_analysis)

#
for simb, scor in sorted(text_analysis.items(), key = lambda x: x[1], reverse = True):
    print('Символ " {} " повторяется {} раз'.format(simb, scor))
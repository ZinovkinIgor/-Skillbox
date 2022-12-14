"""
Задача 1. Согласные
Дан следующий текст:

Even if they are djinns, I will get djinns that can outdjinn them.

Используя регулярные выражения, напишите программу, которая выводит два списка:

Первый содержит все слова, которые начинаются на гласную букву латинского алфавита
(в этот раз слово может состоять и из одной буквы, например I).
Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
Для получения второго списка за основу используйте шаблон, которым вы получили первый список.

Ещё небольшая подсказка: посмотрите, чем отличается символ * от символа +.
Также, когда будете получать второй список, обратите внимание, на какой символ начинаются слова.

Ожидаемый результат:
Слова на гласную: ['Even', 'if', 'are', 'I', 'outdjinn']
Слова на любой символ, кроме гласной: ['they', 'djinns', 'will', 'get', 'djinns', 'that', 'can', 'them']

Задача 2. Даты
Из одного дата-центра пришёл текстовый пакет данных, который содержит информацию о
кодовом названии оборудования, его серийном номере и дате начала эксплуатации.
Вот небольшой кусочек из этого пакета в виде строки:

Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009

Используя регулярные выражения, напишите программу, получающую список всех дат, которые встречаются в строке.

Для этого необходимо использовать \d.

Ожидаемый результат:
['12-05-2007', '11-11-2011', '12-01-2009']
"""

import re

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

    result_1 = re.findall(r'\b[aeouiAEOUI]\w*', text)
    result_2 = re.findall(r'\b[^aeouiAEOUI\W]\w*', text)
    print(result_1)
    print(result_2)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    text_2 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

    result = re.findall(r'\b[0-9]{0,2}\-[0-9]{0,2}\-[0-9]{0,4}\w+', text_2)
    print(result)

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')
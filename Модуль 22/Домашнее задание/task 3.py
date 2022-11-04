"""
Задача 3. Дзен Пайтона 2
Что нужно сделать

Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt
(который содержит всё тот же Дзен Пайтона). Выведите три найденных числа на экран.
Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.
Обратите внимание, что регистр буквы не имеет значение. (А и а - одинаковые буквы).

Формат вывода:
Количество букв в файле:
Количество слов в файле:
Количество строк в файле:
Наиболее редкая буква:
"""


text = open('zen.txt', 'r')
new_text = text.read().lower()
number_word = len(new_text.split(' '))
simbol_text = [simb for simb in new_text if simb.isalpha()]
simbol = len(simbol_text)
string = len(new_text.split('\n'))
print('Количество букв в файле: {}'.format(simbol))
print('Количество слов в файле: {}'.format(number_word))
print('Количество строк в файле: {}'.format(string))
new_dict = dict()
for simb in simbol_text:
    if simb not in new_dict:
        new_dict[simb] = 1
    else:
        new_dict[simb] += 1
min_simb = min(new_dict.values())
for key, value in new_dict.items():
    if value == min_simb:
        print('Наиболее редкая буква: {} повторяется {} раз'.format(key, value))

"""
Задача 8. Частотный анализ
Что нужно сделать

Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ,
определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат
в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части.
Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.

Пример:
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
"""
import string
new_dict = dict()
simbol_dict = dict()
alphabet = string.ascii_letters

text = open('text_1.txt', 'r')
analys = open('analysis.txt', 'a')
text = text.read().lower()
scor = 0
for simb in text:
    if simb in alphabet:
        scor += 1
        if simb in new_dict:
            new_dict[simb] += 1
        else:
            new_dict[simb] = 1
for n in sorted(new_dict.items()):
    simbol_dict[n[0]] = n[1]
for count in sorted(simbol_dict.items(), key=lambda x: x[1], reverse=True):
     print(count[0], round(count[1] / scor, 3))
     analys.write('{} {}\n'.format(
         count[0],
         round(count[1] / scor, 3)))


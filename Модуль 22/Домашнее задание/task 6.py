"""
Задача 6. Паранойя
Что нужно сделать

Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера,
включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря (чем веселит
агента службы безопасности).

Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при этом символы первой
строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее.
Результат выведите в файл cipher_text.txt.

Пример:

Содержимое файла text.txt:
Hello
Hello
Hello
Hello

Содержимое файла cipher_text.txt:
Ifmmp
Jgnnq
Khoor
Lipps
"""

import os
import string
# меняем буквы и возвращаем новую
def cipher_cezar(simb, operation, numb):
    result = (operation.index(simb) + numb) % 24
    return operation[result]

# сохраняем буквы верхний и нижний регистр + символы
simb_lowercase = string.ascii_lowercase
simb_uppercase = string.ascii_uppercase
simb_punct = string.punctuation


"""открываем файл с текстом 
1 циклом проходим по строкам и считаем каждую строку
2 циклом проходим по каждому символу
"""
numb = 0
text = open('text.txt', 'r')
cipher_file = open('cipher_text.txt', 'a')
for word in text:
    numb += 1
    for simb in word:
        if simb in simb_lowercase:
            new_simb = cipher_cezar(simb, simb_lowercase, numb)
            cipher_file.write(new_simb)
        elif simb in simb_uppercase:
            new_simb = cipher_cezar(simb, simb_uppercase, numb)
            cipher_file.write(new_simb)
        else:
            cipher_file.write(simb)
text.close()
cipher_file.close()


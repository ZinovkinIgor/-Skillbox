"""
Задача 1. Python!
Напишите программу, которая выводит в отдельную строчку каждый символ фразы “Python!”.

Задача 2. Вирус
Ваня экспериментирует с различного рода компьютерными вирусами, которые портят жизнь людям.
На просторах Интернета он нашёл код довольно необычного вируса, который “поворачивает”
весь текст в документе и повторяет каждый символ 3 раза.
Пользователь вводит текст. Напишите программу, которая выводит каждый символ текста в отдельной строке и три раза.

Пример:
Введите текст: Привет!
ППП
ррр
иии
ввв
еее
ттт
!!!

Задача 3.
Мы входим в команду разработки нового текстового редактора и нам поручили разработать для него подсчёт
нужного символа в тексте, а именно - буквы Ы. Причём отдельно с верхним регистром и отдельно с нижним.
Напишите программу, которая считает количество больших и количество маленьких букв Ы в тексте и выводит ответ на экран.

Пример:
Введите текст: Прыг скок
Больших букв Ы: 0
Маленьких букв Ы: 1
"""

# Задача 1
print('=' * 40)
print('Задача 1')
text = input('Введите текст: ')
for simbol in text:
    print(simbol)

# Задача 2
print('=' * 40)
print('Задача 2')
text1 = input('Введите текст: ')
for simbol in text1:
    print(simbol * 3)

# Задача 3
print('=' * 40)
print('Задача 3')
text2 = input('Введите текст: ')
big_letter, small_letter = 0, 0
for simbol in text2:
    if simbol == 'Ы':
        big_letter += 1
    if simbol == 'ы':
        small_letter += 1
print('Больших букв Ы:', big_letter)
print('Маленьких букв ы:', small_letter)


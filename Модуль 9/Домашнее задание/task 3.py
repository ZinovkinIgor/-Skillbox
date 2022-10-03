"""
Задача 3. Кривой мессенджер
Что нужно сделать

При передаче сообщений в одном мессенджере иногда возникают неполадки и в сообщение попадает лишний символ - звёздочка.
Пользователям это изрядно надоело, и они начали просто уходить в другие мессенджеры. Хотя одному пользователю стало интересно,
на каких обычно позициях появляется эта звёздочка.
Чтобы это выяснить, пользователю необходимо подготовить строки в которых символ “*” встречается ровно один раз.
Напишите программу, которая определяет порядковый номер этого символа в строке.

Пример:
Введите текст: Пр*ивет как дела
Символ ‘*’ стоит на позиции 3
"""

text = input('Введите текст: ')
score = 0
for simbol in text:
    score += 1
    if simbol == '*':
        print('Символ "*" стоит на позиции: ', score)
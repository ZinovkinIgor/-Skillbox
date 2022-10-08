"""
Задача 4. Урок информатики 3
Что нужно сделать

Наконец-то учитель смог объяснить детям, что такое эта «плавающая точка». Однако долго его радость не продлилась,
ведь на следующем уроке нужно будет объяснить такие страшные слова, как «экспоненциальное», «мантисса» и «порядок».
Хоть старшеклассники и знакомы с экспонентой, учитель всё равно не уверен, что здесь всё будет понятно.
Поэтому для наглядности он также написал программу.
На вход подаётся строка — это экспоненциальная форма числа. Напишите программу, которая выводит отдельно мантиссу
и отдельно порядок этого числа.
"""

def func_number(n):
    score = 0
    if n < 1:
        while 0 < n < 1:
            n *= 10
            score += 1
        print('Мантисса: ', n, 'порядок: -', score)
    else:
        while 1 < n > 10:
            n /= 10
            score += 1
        print('Мантисса: ', n, 'порядок:', score)

number = float(input('введите число: '))
func_number(number)








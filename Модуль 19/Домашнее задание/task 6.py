"""
Задача 6. Словарь синонимов
Что нужно сделать
Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. На вход в программу подаётся N пар слов.
Каждое слово является синонимом к своему парному слову.
Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя
слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, то выведите ошибку и
запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.
Пример:
Введите количество пар слов: 3
Первая пара: Привет — Здравствуйте
Вторая пара: Печально — Грустно
Третья пара: Весело — Радостно

Введите слово: интересно
Такого слова в словаре нет.
Введите слово: здравствуйте
Синоним: Привет
"""

scor = int(input('Введите количество пар слов: '))
word_dict = dict()
for num in range(1, scor + 1):
    print(num, 'пара: ', end='')
    couple_word = input().split(' - ')
    word_dict[couple_word[0]] = couple_word[1]

while True:
    search_word = input('Введите слово: ')
    if search_word == 'end':
        break
    if search_word in word_dict.keys():
        print('Синоним:', word_dict[search_word])
    elif search_word in word_dict.values():
        for simb, value in word_dict.items():
            if search_word == value:
                print('Синоним:', simb)
    else:
        print('Такого слова в словаре нет.')





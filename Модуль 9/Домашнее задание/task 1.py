"""
Задача 1. Календарь
Что нужно сделать

Мы продолжаем разрабатывать удобный календарь для смартфона.
Функцию определения високосного года мы добавили, но забыли ещё много разных очевидных вещей.
Напишите программу, которая принимает от пользователя день недели в виде строки и выводит его номер на экран.

Пример:
Введите день недели: вторник
Номер дня недели: 2
"""

search_day = input('Введите день недели: ')
score = 0
for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
    score += 1
    if search_day == day:
        break
print('Номер дня недели: ', score)
"""
Задача 10. Пропавшая карточка
Что нужно сделать

Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Напишите программу,
которая поможет найти потерянную карточку, если номера оставшихся известны. Найдите её, зная номера оставшихся карточек.
Введите число карточек — N.
Затем введите N - 1 номера оставшихся карточек. Они могут быть введены в любом порядке.

Пример:
Введите количество карточек: 5
Введите номер оставшейся карточки: 1
Введите номер оставшейся карточки: 4
Введите номер оставшейся карточки: 5
Введите номер оставшейся карточки: 3
Номер пропавшей карточки: 2
"""

summ1, summ2 = 0, 0
card = int(input('Введите количество карточек: '))
for num in range(1, card + 1):
    summ1 += num
for _ in range(1, card):
    num_card = int(input('Введите номер оставшейся карточки: '))
    summ2 += num_card
print('Номер пропавшей карточки:', summ1 - summ2)






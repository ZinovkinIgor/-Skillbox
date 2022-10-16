"""
Задача 4. Товары
Что нужно сделать
В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров,
второй — за списки количества разнообразных товаров на складе:
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за одну штуку).
Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
Результат работы программы:
Лампа — 27 штук, стоимость 1134 рубля
Стол — 54 штуки, стоимость 27 860 рублей
Диван — 3 штуки, стоимость 3550 рублей
Стул — 105 штук, стоимость 10 311 рублей
"""


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, value in goods.items():
    sum_price = 0
    scor_store = 0
    for num in store[value]:
        scor_store += num['quantity']
        sum_price += num['quantity'] * num['price']

    print('{} — {} штук, стоимость {} рубля'.format(key, scor_store, sum_price))




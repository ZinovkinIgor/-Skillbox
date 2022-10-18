"""
Задача 7. Пицца
Что нужно сделать
В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них в определённый период.
Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.
На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название пиццы —
количество заказанных пицц». Реализуйте код, который выводит список покупателей и их заказов по алфавиту. Учитывайте,
что один человек может заказать одно и то же несколько раз.

Пример:
Введите количество заказов: 6
Первый заказ: Иванов Пепперони 1
Второй заказ: Петров Де-Люкс 2
Третий заказ: Иванов Мясная 3
Четвёртый заказ: Иванов Мексиканская 2
Пятый заказ: Иванов Пепперони 2
Шестой заказ: Петров Интересная 5

Иванов:
    Мексиканская: 2
    Мясная: 3
    Пепперони: 3
Петров:
    Де-Люкс: 2
    Интересная: 5
"""


scor = int(input('Введите количество заказов: '))
order_dict = dict()
for num in range(1, scor + 1):
    print('{} заказ: '.format(num), end='')
    order = input().split()
    if order[0] not in order_dict:
        order_dict[order[0]] = {}
        order_dict[order[0]][order[1]] = int(order[2])
    elif order[1] not in order_dict[order[0]]:
        order_dict[order[0]][order[1]] = int(order[2])
    else:
        order_dict[order[0]][order[1]] += int(order[2])


for human in order_dict:
    print(human)
    for res_order in order_dict[human]:
        print('\t{}: {}'.format(res_order, order_dict[human][res_order]))










"""
Задача 1. Машина 2
Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
цвет машины (например, красный),
цена (один миллион),
максимальная скорость (200),
текущая скорость (ноль).

Добавьте два метода класса:
Отображение информации об объекте класса.
Метод, который позволяет устанавливать текущую скорость машины.
Проверьте работу этих методов.

Задача 2. Семья
Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и
объекты которого могут выполнять следующие действия:
Отобразить информацию о себе.
Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести соответствующее сообщение об
успешной/неуспешной покупке дома.
Создайте как минимум один экземпляр класса и проверьте работу методов.

Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
Family name: Common family
Family funds: 100000
Having a house: False

Try to buy a house
Not enough money!

Earned 800000 money! Current value: 900000
Try to buy a house again
House purchased! Current money: 0.0

Family name: Common family
Family funds: 0.0
Having a house: True
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    import random

    class MyAuto():
        color = 'Red'
        price = '1600000'
        speed_max = '220'
        speed_curron = '100'

        def info_auto(self):
            print('Цвет: {color}\nСтоимост: {price}\nМаксимальная скорость: {max_speed}\nТекущая скорость: {cur_speed}'.format(
                color = self.color,
                price = self.price,
                max_speed = self.speed_max,
                cur_speed = self.speed_curron
            ))

        def curron(self):
            self.speed_curron = random.randint(0, 200)


    auto_1 = MyAuto()
    auto_2 = MyAuto()
    auto_1.curron()
    auto_1.info_auto()
    auto_2.info_auto()





elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    class Family():
        surmane = 'Surname'
        money = 100000
        house = False

        def incom(self, salary):
            self.money += int(salary)
            print('Вы смогли отложить {} на дом. Сумма ваших накопдений {}'.format(salary, self.money))

        def bay_house(self, price, sale=0):
            price_house = price * sale / 100
            if price_house <= self.money:
                self.money -= price_house
                self.house = True
                print('Вы купили дом поздравляю за {} рублей. У Вас осталось денег {}'.format(price_house, self.money))
            else:
                print('Вы не купили дом за {} рублей. У Вас осталось денег {}'.format(price_house, self.money))

        def info_surname(self):
            print('Фамилия: {}\nКапитал:{}\nНаличие дома:{}\n\n'.format(self.surmane, self.money, self.house))


    family_1 = Family()
    family_2 = Family()
    family_1.surmane = 'Зиновкины'
    family_2.surmane = 'Петровы'
    family_1.info_surname()
    family_2.info_surname()
    family_1.incom(19 ** 6)
    family_1.bay_house(16 ** 6, 28)
    family_1.info_surname()
    family_2.incom(9 ** 5)
    family_2.bay_house(12 ** 5, 9)
    family_2.info_surname()





elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
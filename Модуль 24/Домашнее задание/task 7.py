"""
Задача 7. Совместное проживание
Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или всё же лучше остаться в гордом одиночестве, Артём решил провести
довольно необычное исследование. Для этого он реализовал модель человека и модель дома.
Человек может:
Есть (+ сытость, − еда).
Работать (− сытость, + деньги).
Играть (− сытость).
Ходить в магазин за едой (+ еда, − деньги).
У человека есть имя, степень сытости (изначально 50) и дом.
В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, то человек умирает.
Логика действий человека определяется следующим образом:
Генерируется число кубика от 1 до 6.
Если сытость < 20, то поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.
Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.
Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.
Надеемся, эти люди живы...
"""

import random

class Human:
    """
    Класс человек:
        аргументы:
            - сытость;
        методы:
            - есть;
            - работать;
            - играть;
            - ходить в магазин за едой;
            - жизнь.
    """
    satiety = 50


    def __init__(self, name):
        self.name = name
        self.satiety = Human.satiety
        self.summ_money = 0
        self.day_play = 0
        self.eart = 0
        self.market = 0
        self.kwork = 0



    def life(self, day):
        "Симулятор жизни"
        cube = random.randint(1, 6)

        if self.satiety == 0:
            raise ("Умер с голода.")

        elif self.satiety < 20 and Fridge.food_supply > 2:
            "Если сытость < 20 и еды больше 2, то поесть"
            self.satiety += 2
            Fridge.get_food(self.name)
            print('{} Покушал, его сытость = {}. Денег осталось {}'.format(
                self.name,
                self.satiety,
                Financial_transactions.bank_account
            ))
            self.eart += 1

        elif Fridge.food_supply < 10 and Financial_transactions.bank_account > 2:
            "Иначе, если еды в доме < 10  и денег больше 5, то сходить в магазин."
            Fridge.refill_refrigerator(self.name)
            Financial_transactions.make_waste(self.name)
            print('{} Сходил в магазин, Купил еды и заполнил холодильник = {}. Денег осталось {}'.format(
                self.name,
                Fridge.food_supply,
                Financial_transactions.bank_account
            ))
            self.market += 1

        elif Financial_transactions.bank_account < 50:
            "Иначе, если денег в доме < 50, то работать."
            self.satiety -= 1
            Financial_transactions.earn_money(self.name)

            print('{} Сходил на работу. Денег осталось {}'.format(
                self.name,
                Financial_transactions.bank_account
            ))
            self.kwork += 1
            self.summ_money += 2

        elif cube == 1:
            "Иначе, если кубик равен 1, то работать."
            self.satiety -= 1
            Financial_transactions.earn_money(self.name)

            print('{} Сходил на работу. Денег осталось {}'.format(
                self.name,
                Financial_transactions.bank_account
            ))
            self.kwork += 1
            self.summ_money += 2

        elif cube == 2:
            "Иначе, если кубик равен 2, то поесть."
            self.satiety += 2
            Fridge.get_food(self.name)
            print('{} Покушал, его сытость = {}. Денег осталось {}'.format(
                self.name,
                self.satiety,
                Financial_transactions.bank_account
            ))
            self.eart += 1

        else:
            "Человек играет."
            self.satiety -= 1

            print('{} играет. Осталось сытости {}'.format(
                self.name,
                self.satiety
            ))
            self.day_play += 1

    def print_info(self):
        print('За время жизни {} заработал {} денег, сходил в магазин {} раз. Купил {} еды, Проиграл {} дней'.format(
            self.name,
            self.summ_money,
            self.market,
            self.eart,
            self.day_play
        ))

class Kids:
    satiety = 50


    def __init__(self, name):
        self.name = name
        self.satiety = Human.satiety
        self.day_play = 0
        self.eart = 0

    def life(self, day):
        "Симулятор жизни"
        cube = random.randint(1, 6)

        if self.satiety == 0:
            raise ("Умер с голода.")

        elif self.satiety < 20:
            "Если сытость < 20 и еды больше 2, то поесть"
            self.satiety += 2
            Fridge.get_food(self.name)
            print('{} Покушал, его сытость = {}. Денег осталось {}'.format(
                self.name,
                self.satiety,
                Financial_transactions.bank_account
            ))
            self.eart += 1

        else:
            "Человек играет."
            self.satiety -= 1
            self.day_play += 1

    def print_info(self):
        print('За время жизни {} покушал {} еды, Проиграл {} дней'.format(
            self.name,
            self.eart,
            self.day_play
        ))



class Fridge:
    """
    Класс холодильник:
        аргументы:
            - количество еды
        методы:
            - пополнить холодильник;
            - забрать с холодильника.
    """

    food_supply = 50

    def refill_refrigerator(self):
        "Пополнить холодильник продуктами."
        Fridge.food_supply += 2

    def get_food(self):
        "Достать еду из холодильника."
        Fridge.food_supply -= 1

class Financial_transactions:
    """
     Финансовые операции:
        аргументы:
            - количество денег.
        методы:
            - пополнить счет;
            - произвести трату.
    """

    bank_account = 0

    def earn_money(self):
        "Внести на счет заработанные деньги"
        Financial_transactions.bank_account += 2

    def make_waste(self):
        "Потратить деньги"
        Financial_transactions.bank_account -= 2


name_1 = Human('Bob')
name_2 = Human('Kriss')
kids_1 = Kids('Robby')
kids_2 = Kids('Teddy')
kids_3 = Kids('Anna')
for num in range(365):
    print('\nНаступил день {}.'.format(num))
    name_1.life(num)
    name_2.life(num)
    kids_1.life(num)
    kids_2.life(num)
    kids_3.life(num)
name_1.print_info()
name_2.print_info()
kids_1.print_info()
kids_2.print_info()
kids_3.print_info()



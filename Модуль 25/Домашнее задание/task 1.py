"""
Задача 1. Налоги
Что нужно сделать

Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property
и производных от него классов Apartment, Car и CountryHouse.
Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога,
переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости,
на машину — 1/200, на дачу — 1/500.
Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.
Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость
имущества, а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).
"""


class Property:
    """
    Родительский класс.
    worth - количество денег
        :rtype int
    calculation_tax - расчет налога на имущество
        :return - стоимость налога, или сколько нехватает
        :rtype str
    """
    def __init__(self, worth):
        self.worth = worth

    def calculation_tax(self, price):
        price_tax = price / 1000
        if self.worth >= price_tax:
            return 'Стоимость налога на квартиру: {}'.format(price_tax)
        else:
            result = price_tax - self.worth
            return 'У вас недостаточно денег. Нехватает {} рублей'.format(result)

class Flat(Property):
    """
    Дочерний класс, квартира.
    """
    pass

class Car(Property):
    """
    Дочерний класс, машина.
    """
    def calculation_tax(self, price):
        price_tax = price / 200
        if self.worth >= price_tax:
            return 'Стоимость налога на машину: {}'.format(price_tax)
        else:
            result = price_tax - self.worth
            return 'У вас недостаточно денег. Нехватает {} рублей'.format(result)


class House(Property):
    """
    Дочерний класс, Дача.
    """
    def calculation_tax(self, price):
        price_tax = price / 500
        if self.worth >= price_tax:
            return 'Стоимость налога на дачу: {}'.format(price_tax)
        else:
            result = price_tax - self.worth
            return 'У вас недостаточно денег. Нехватает {} рублей'.format(result)


my_flat = Flat(700)
print(my_flat.calculation_tax(3000000))
my_car = Car(70000)
print(my_car.calculation_tax(3300000))
my_house = House(9000)
print(my_house.calculation_tax(70000000))







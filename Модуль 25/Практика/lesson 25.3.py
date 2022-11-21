"""
Задача 1. Корабли
Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может сделать
два действия: сообщить свою модель и идти по воде.

Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия:
погрузить и выгрузить груз с корабля.
У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также, вместо
погрузки и выгрузки, у него есть другое действие — атаковать.
Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс
«Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.

Задача 2. Роботы
На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного разные
функции. У каждого робота есть номер модели и действие operate, которое означает, что делает робот. Особенности роботов следующие:

У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он пылесосит
пол, и выводит текущую заполняемость мешка.
У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого оружия.
Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины, и при команде
operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
Напишите программу, которая реализует все необходимые классы роботов.

Задача 3. Кастомные исключения
Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
И для создания своего собственного класса ошибки достаточно написать его дочерний класс. Например:

class MyOwnException(Exception):
    pass

raise MyOwnException('Это моя ошибка!')

Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), чтобы не сломать автоматические
обработчики исключений.
Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на второе и выводит
ответ на экран. Если первое число меньше второго, то программа выдаёт исключение DivisionError (нельзя делить меньшее на большее).

Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.
"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)


    class Ship:
        def __init__(self, model):
            self.model = model

        def __str__(self):
            return 'Корабль: {}'.format(self.model)

        def sail(self):
            print('Корабль плывет вперед.')

    class WarShip(Ship):
        def __init__(self, model, weapon):
            super().__init__(model)
            self.weapon = weapon

        def shoot(self):
            print('Корабль {} стреляет из {}'.format(self.model, self.weapon))

    class TransportShip(Ship):
        max_hold = 10
        def __init__(self, model):
            super().__init__(model)
            self.hold = 0

        def loading(self):
            if self.hold < self.max_hold:
                self.hold += 1
                print('Производим загрузку. Загружено {} тонн'.format(self.hold))
            else:
                print('Корабль {} загружен полностью {}'.format(self.model, self.hold))

        def unloading(self):
            if self.hold > 0:
                self.hold -= 1
                print('Производим разгрузку. Загружено {} тонн'.format(self.hold))
            else:
                print('Корабль {} пустой'.format(self.model))


    shhip_1 = WarShip('Патриот', 'Пушки')
    print(shhip_1)
    shhip_1.shoot()
    shhip_1.sail()
    shhip_2 = TransportShip('Титаник')
    for _ in range(11):
        shhip_2.loading()
    for _ in range(11):
        shhip_2.unloading()

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Robot:
        def __init__(self, numbers):
            self.__numbers = numbers


        def operate(self):
            return self.__numbers

    class RobotCleaner(Robot):
        bag = 0
        max_bag = 15
        def __init__(self, numbers):
            super().__init__(numbers)

        def operate_cleaner(self):
            if self.bag < self.max_bag:
                self.bag += 1
                print('{} Робот пылесос производит уборку, заполняемость мешка {} кг.'.format(
                    self.operate(), self.bag)
                )
            else:
                print('Робот пылесос заполнен. Необходима очистка.')

    class MilitaryRobot(Robot):
        def __init__(self, numbers, weapon):
            super().__init__(numbers)
            self.weapon = weapon

        def operate_war(self):
            print('{} Робот обороняет склад с помощью оружия {}.'.format(self.operate(), self.weapon))

    class Submarine(MilitaryRobot):
        def __init__(self, numbers,  weapon, depth):
            super().__init__(numbers, weapon)
            self.depth = depth

        def operate_sub(self):
            print('{} Робот охраняет объект с помощью оружия {}. Под водой на глубине {} метров'.format(
                self.operate(), self.weapon, self.depth)
            )

    dron_1 = RobotCleaner(333)
    dron_2 = MilitaryRobot(1234, 'Плазменная пушка')
    dron_3 = Submarine(985, 'Торпеда', 800)
    dron_1.operate_cleaner()
    dron_2.operate_war()
    dron_3.operate_sub()

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


    class Equation:
        def __init__(self, divisible, divisor):
            self.divisible = divisible
            self.divisor = divisor

        def decision(self):
            try:
                if self.divisible <= self.divisor:
                    raise Exception
                else:
                    print('{} / {} = {}'.format(
                        self.divisible, self.divisor, self.divisible / self.divisor
                    ))
            except Exception:
                print('Делимое должно быть больше делителя.')


    numbers = open('numbers.txt')
    for line in numbers:
        numb = line.split()
        try:
            if isinstance(numb[0] or numb[1], str):
                divisibre = int(numb[0])
                divisor = int(numb[1])
                example = Equation(divisibre, divisor)
                example.decision()
        except IndexError:
            print('В уровнении должно быть 2 значения')
        except ValueError:
            print('В уровнении  должны быть числа')
    numbers.close()

else:
    print('Выберите задачу заново.')
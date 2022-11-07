"""
Задача 1. Машина 3
Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
Четыре атрибута:
цвет машины (например, красный),
цена (один миллион),
максимальная скорость (200),
текущая скорость (ноль).
Два метода:
Отображение информации об объекте класса.
Метод, который позволяет устанавливать текущую скорость машины.
Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
Реализуйте такое изменение класса.

Задача 2. Координаты точки
Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться пользовательские
значения координат, по умолчанию x = 0, y = 0.
Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет информацию о ней.
Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.

Задача 3. Весёлая ферма
Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и расти.
Всего у картошки может быть четыре стадии зрелости.
Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
а также предоставлять информацию о зрелости всей картошки на своей территории.

Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.

Пример результата (проверка на зрелость и три взращивания):
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Росток
Картошка 2 сейчас Росток
Картошка 3 сейчас Росток
Картошка 4 сейчас Росток
Картошка 5 сейчас Росток
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Зелёная
Картошка 2 сейчас Зелёная
Картошка 3 сейчас Зелёная
Картошка 4 сейчас Зелёная
Картошка 5 сейчас Зелёная
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Зрелая
Картошка 2 сейчас Зрелая
Картошка 3 сейчас Зрелая
Картошка 4 сейчас Зрелая
Картошка 5 сейчас Зрелая
Вся картошка созрела. Можно собирать!
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    import random

    class Auto:
        car_brand = ['Audi', 'BMW', 'KIA', 'Lexus', 'Nissan', 'Jeep', 'Lada']
        car_colors = ['Белый', 'Черный', 'Зеленый', 'Красный', 'Синий', 'Желтый', 'Коричневый']

        def __init__(self, name, speed_max, total_speed):
            self.name = name
            self.speed_max = speed_max
            self.total_speed = total_speed

        def print_info(self):
            print('Владелец автомобиля: {name}\nМарка: {brand}\nЦвет: {color}\nМаксимальная скорость: {speed_max}\nСкорость движения: {speed_total}'.format(
                name=self.name,
                brand=random.choice(Auto.car_brand),
                color=random.choice(Auto.car_colors),
                speed_max=self.speed_max,
                speed_total=self.total_speed))

    my_car_1 = Auto('Игорь', 250, 110)
    my_car_2 = Auto('Никита', 200, 99)
    my_car_1.print_info()
    my_car_2.print_info()


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    class Point:
        count = 0

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
            Point.count += 1

        def print_info(self):
            print('Всего точек {count}\n Точка находится по координатам (x = {x} y = {y})'.format(
                count=Point.count,
                x=self.x,
                y=self.y))

    mypoint_1 = Point(1, 9)
    mypoint_2 = Point(7, 2)
    mypoint_3 = Point()
    mypoint_4 = Point(5, 1)
    mypoint_5 = Point(9, 7)

    mypoint_1.print_info()
    mypoint_2.print_info()
    mypoint_3.print_info()
    mypoint_4.print_info()
    mypoint_5.print_info()

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


    class Potato:

        status = {0: 'Посадили', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

        def __init__(self, index):
            self.index = index
            self.state = 0

        def sprouts(self):
            if self.state < 3:
                self.state += 1
            self.print_garden()

        def print_garden(self):
            print('Картошка {} в стадии {}'.format(self.index, Potato.status[self.state]))

        def result(self):
            if self.state == 3:
                return True
            return False


    class PotatoGarden:

        def __init__(self, count):
            self.potatos = [Potato(index) for index in range(1, count + 1)]

        def plant(self):
            print('Картошка проростает')
            for i_patato in self.potatos:
                i_patato.sprouts()

        def plant_potato(self):
            if not all([i_potato.result() for i_potato in self.potatos]):
                print('Картошка еще не созрела.')
            else:
                print('Картошка созрела, можно собирать урожай.')

    my_garden = PotatoGarden(5)
    for _ in range(3):
        my_garden.plant()
        my_garden.plant_potato()


else:
    print('Выберите задачу заново.')
"""
Задача 3. Круг
Что нужно сделать
На координатной плоскости рисуются круги, у каждого круга следующие параметры: координаты X и Y центра круга и значение
R ― радиус круга. По умолчанию центр находится в (0, 0), а радиус равен 1.

Реализуйте класс «Круг», который инициализируется по этим параметрам. Круг также может:
Находить и возвращать свою площадь.
Находить и возвращать свой периметр.
Увеличиваться в K раз.
Определять, пересекается ли он с другой окружностью.
"""


import random
import math

class Cyrcle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.print_cyrcle()


    def square(self):
        self.square_cyrcle = math.pi * self.r ** 2
        return self.square_cyrcle


    def perimeter(self):
        self.perimeter_cyrcle = 2 * math.pi * self.r
        return self.perimeter_cyrcle

    def increase(self):
        self.r = self.r * random.randint(1, 10)
        return self.r

    def print_cyrcle(self):
        print('Площадь круга: {}\nПериметр круга: {}\nУвеличиваем в {} раз\n'.format(
            self.square(),
            self.perimeter(),
            self.increase()
        ))


exemple = Cyrcle(3, 5, 3)
exemple.print_cyrcle()
exemple.print_cyrcle()




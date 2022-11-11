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


import math

class Circle():
    '''Добавляем данные по окружности (х,у,r)'''

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area_search(self):
        '''Находит и выводит площадь окружности'''
        self.square = math.pi * self.r ** 2

    def perimeter_search(self):
        '''Находит периметр'''
        self.perimeter = 2 * math.pi * self.r

    def increase(self):
        '''Увеличить в К раз'''
        k = int(input('Восколько раз увеличить окружность: '))
        self.r = self.r * k
        print('Изменение окружности после увеличения.')
        self.area_search()
        self.perimeter_search()
        self.print_circle()

    def intersection(self):
        '''Проверяем пересечение окружностей.'''
        self.distance = ((circle_1.x - circle_2.x) ** 2 + (circle_1.y - circle_2.y) ** 2)
        if self.distance == 0:
            print('Окружность 1 входит в окружность 2' if circle_1.r > circle_2.r else 'Окружность 2 входит в окружность 1')
        elif self.distance < (circle_1.r + circle_2.r) ** 2:
            print('Окружности пересекаются.')
        else:
            print('Окружности не пересекаются.')

    def print_circle(self):
        '''Вывод на экран'''
        print('Площадь окружности: {}\nПериметр окружности: {}\n\n'.format(self.square, self.perimeter))


    def  launching_programm(self):
        '''Запуск программы'''
        self.area_search()
        self.perimeter_search()
        self.print_circle()
        self.increase()
        self.intersection()


circle_1 =Circle(4, 3, 3)
circle_2 =Circle(0, 0, 1)
circle_1.launching_programm()
circle_2.launching_programm()




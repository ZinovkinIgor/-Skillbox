"""
Задача 2. Математический модуль
Что нужно сделать
Вася использует в своей программе очень много различных математических вычислений, связанных с фигурами.
Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством функций,
он решил выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем math.

Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

вычисление длины окружности,
вычисление площади окружности,
вычисление объёма куба,
вычисление площади поверхности сферы.
Пример основного кода:

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)


Результат:

31.41592653589793

113.09733552923255
"""

import math
from abc import ABC, abstractmethod

class MyMath(ABC):
    """ Формулы расчета"""

    def circle_len(radius: int) -> float:
        """
        Расчет длинны окружности
        на ввод радиус
        :return: result
        """
        result = 2 * math.pi * radius
        return result

    def circle_sq(radius: int) -> float:
        """
        Расчет площади окружности
        на ввод радиус
        :return: result
        """
        result = math.pi * radius ** 2
        return result

    def cube_volume( volume: int) -> float:
        """
        Расчет объема куба
        на ввод длинна стороны
        :return: result
        """
        result = volume ** 3
        return result

    def surface_sphere(radius: int) -> float:
        """
        Расчет площади поверхности сферы
        на ввод радиус
        :return: result
        """
        result = 4 * math.pi * radius ** 2
        return result

    def ball_volume(radius: int) -> float:
        """
        Расчет объема шара
        на ввод радиус
        :return: result
        """
        result = 4 / 3 * math.pi * radius ** 3
        return result

result_1 = MyMath.circle_len(radius = 5)
result_2 = MyMath.circle_sq(radius = 6)
result_3 = MyMath.cube_volume(volume = 9)
result_4 = MyMath.surface_sphere(radius = 5)
result_5 = MyMath.ball_volume(radius = 5)

print('Длинна окружности: {}'.format(result_1))
print('Площадь окружности: {}'.format(result_2))
print('Объем куба: {}'.format(result_3))
print('Площадь поверхности сферы: {}'.format(result_4))
print('Объем шара: {}'.format(result_5))



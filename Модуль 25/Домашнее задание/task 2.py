"""
Задача 2. Карма
Что нужно сделать

Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и
может с вероятностью 1 к 10 выкинуть одно из исключений:

KillError;
DrunkError;
CarCrashError;
GluttonyError;
DepressionError.
Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при
накоплении кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.
"""


import random


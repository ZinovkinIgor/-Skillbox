"""
Задача 5. Ускоряем работу функции
Что нужно сделать
У нас есть функция, которая делает определённые действия с входными данными:
берёт факториал от числа;
результат делит на куб входного числа;
получившееся число возводит в 10-ю степень.
def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result
Однако каждый раз нам приходится делать сложные вычисления, хотя входные и выходные данные одни и те же.
И тут наши знания тонкостей Python должны нам помочь.
Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз.
Подсказка: вспомните, что происходит с изменяемыми данными, если их выставить по умолчанию в параметрах функции.
"""

import math

def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result

def calculating_math_func_2(data):

    result = (math.factorial(data) / data ** 3) ** 10
    return result

print(calculating_math_func(10))

print(calculating_math_func_2(10))
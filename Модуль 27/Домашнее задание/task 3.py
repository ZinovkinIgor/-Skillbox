"""
Задача 3. Логирование
Что нужно сделать

Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции и
её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
записываются названия функции и ошибки.
Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
"""

from typing import Callable
from datetime import datetime
import time
import functools

def timer(func: Callable) -> Callable:
    """
    Функция timer. Рассчитывает время работы функции.
    """
    @functools.wraps(func)
    def wrappend_func(*args, **kwargs) -> Callable:
        start_func = time.time()
        try:

            func(*args, **kwargs)
            end_func = time.time()
            print('Время работы программы {res}'.format(
                res=end_func - start_func
            ))
            return func
        except ValueError:
            print('Ошибка. Введены некорректные данные')
    return wrappend_func

def logging(func: Callable) -> Callable:
    """
    Выводит на экран название функции, аргументы и документацию функции.
    """
    @functools.wraps(func)
    def wrappend_func(*args, **kwargs) -> Callable:
        print('Название функции: {name}\nПозиционные аргументы: {args}\nИменованые аргументы: {kwargs}\n\n'
              'Документация функции: \n{docs}\n'.format(
            name=func.__name__, args=args, kwargs=kwargs, docs=func.__doc__
        ))
        func(*args, **kwargs)
        return func
    return wrappend_func

@timer
@logging
def cube_func(number):
    """Функция считаем сумму возведенных в куб"""
    cube = sum(numb ** 3 for numb in range(number))
    print('Сумма чисел возведенных в куб: {cube}'.format(cube=cube))

numder = int(input('Введите число: '))
cube_func(numder)












"""
Задача 2. Замедление кода
Что нужно сделать

В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный пример — функция,
которая постоянно проверяет, изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

"""
from typing import Callable
import functools
import time

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrappend_func(*args, **kwargs):
        print('Идет работа функции.....')
        start_func = time.time()
        func(*args, **kwargs)
        end_func = time.time()
        print('Время работы программы: {}'.format(end_func-start_func))
        return func

    return wrappend_func

def sleep_func(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrappend_func(*args, **kwargs):
        time.sleep(4)
        print('Задержка 4 секунды')
        func(*args, **kwargs)
        return func
    return wrappend_func
@timer
@sleep_func
def squard(number: int) -> None:
    summ = sum(numb ** 2 for numb in range(number))
    print('Сумма чисел {}'.format(summ))


squard(100)

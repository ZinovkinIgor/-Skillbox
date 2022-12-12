"""
Задача 3. Логирование в формате
Что нужно сделать
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и в
который можно передавать формат вывода даты и времени логирования.

Пример кода, передаётся формат «месяц день год — часы:минуты:секунды»:

@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


Результат:
Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Тут метод test_sum_1.
Завершение 'A.test_sum_1', время работы = 0,187 s.
Тут метод test_sum_1 у наследника.
Завершение 'B.test_sum_1', время работы = 0,187 s.
Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37.
Тут метод test_sum_2 у наследника.
Завершение 'B.test_sum_2', время работы = 0,370 s.

Совет: внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями в этой задаче.
"""

import functools
from datetime import datetime
from _collections_abc import Callable
import time


def timer(cls):
    """
    Декоратор.
    Выводит время запуска и таймер считает время работы функции.
    """
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        print('Запускается \'{func}.{name}\'. Дата и время запуска: {date}'.format(
            func=wrapped.__qualname__, name=cls.__name__, date=datetime.utcnow()
        ))
        start_time = time.time()
        time_n = cls(*args, **kwargs)
        end_time = time.time()
        print('Завершение \'{func}.{name}\' Время работы {time}s'.format(
            func = wrapped.__qualname__, name = wrapped.__name__, time = round(end_time - start_time, 3)))
        return time_n
    return wrapped

def log_methods(createtime: Callable) -> Callable:
    '''
    Запускаем декоратор и применяем декоратор timer ко всем функциям
    '''
    createtime = timer
    @functools.wraps(createtime)
    def time_func(cls):
        for i_file in dir(cls):
            if i_file.startswith('__') is False:
                new_method = getattr(cls, i_file)
                decorator_method = createtime(new_method)
                setattr(cls, i_file, decorator_method)
        return cls
    return time_func



@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
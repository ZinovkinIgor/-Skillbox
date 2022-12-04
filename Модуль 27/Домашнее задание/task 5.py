"""
Задача 5. Счётчик
Что нужно сделать

Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
"""

import functools
from typing import Callable
import random

def counter(func: Callable) -> Callable:
    '''Запускаем декоратор счетчик'''
    @functools.wraps(func)
    def wrappend(*args, **kwargs):
        wrappend.count += 1
        return func(*args, **kwargs)
    wrappend.count = 0
    return wrappend

@counter
def test():
    pass

@counter
def test1():
    pass

for _ in range(random.randint(1, 9999)):
    test()
for _ in range(random.randint(1, 9999)):
    test1()

print('Количество вызовов test {} раз'.format(test.count))
print('Количество вызовов test1 {} раз'.format(test1.count))


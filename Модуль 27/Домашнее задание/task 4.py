"""
Задача 4. Дебаг
Что нужно сделать

Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя
(вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
После этого выводится результат её выполнения.

Пример декорируемой функции:

def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

Основной код:

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

Результат:
Вызывается greeting('Том')
'greeting' вернула значение 'Привет, Том!'
Привет, Том!

Вызывается greeting('Миша', age=100)
'greeting' вернула значение 'Ого, Миша! Тебе уже 100 лет, ты быстро растёшь!'
Ого, Миша! Тебе уже 100 лет, ты вырос!

Вызывается greeting(name='Катя', age=16)
'greeting' вернула значение 'Ого, Катя! Тебе уже 16 лет, ты быстро растёшь!'
Ого, Катя! Тебе уже 16 лет, ты быстро растешь!

Совет: попробуйте самостоятельно изучить функцию repr. Это поможет в решении задачи.

"""
import functools
from typing import Callable

def debug(func: Callable) -> Callable:
    '''
    функция получает имя и возраст,
    выводит на экран 1 значение, далее выполняется функция
    и выводится далее вся функция
    '''
    @functools.wraps(func)
    def wrappend(*args, **kwargs):
        print('\nВызывается {func}{args} {kwargs}'.format(
            func=func.__name__, args=[repr(numb) for numb in args],
            kwargs=[(key, value) for key, value in kwargs.items()]))
        result = func(*args, **kwargs)
        print('\'{func}\' вернула значение \'{result}\''.format(func=func.__name__, result=result))
        print(result)
        return  result
    return wrappend

@debug
def greeting(name, age=None):
    '''Если есть значение возраст, то возвращаем (Ого, {name}! Тебе уже {age} лет, ты быстро растешь!)
    иначе Привет, {name}! '''
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)


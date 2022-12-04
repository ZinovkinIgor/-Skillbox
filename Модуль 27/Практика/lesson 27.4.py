"""
Задача 1. Сэндвич
Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные ингредиенты вроде салата,
помидоров и других. Всё это в свою очередь содержится между двух половинок булочки. Реализуйте такую функцию и
два соответствующих декоратора — ингредиенты и хлеб.
Пример результата работы программы при вызове функции sandwich:
</----------\>
#помидоры#
--ветчина--
~салат~
<\______/>

Задача 2. Плагины
Один проект состоит из огромного количества разнообразных функций, часть из которых используется в других
проектах в качестве плагинов, то есть они как бы «подключаются» и создают дополнительный функционал.
Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить их
в соответствующий словарь.
"""

from typing import Callable, Any
import random
import time

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    def bread(func: Callable) -> Callable:
        """Функция декоратор """
        def wrapped_func(*args, **kwargs) -> None:
            print('</{simb}\>'.format(simb='-' * 6))
            func(*args, **kwargs)
            print('<\{simb}/>'.format(simb='-' * 6))
            return
        return wrapped_func

    def greenery(func: Callable) -> Callable:
        """Функция декоратор """
        def wrapped_func(*args, **kwargs) -> None:
            print('#Помидоры#')
            func(*args, **kwargs)
            print('зелень')
            return

        return wrapped_func

    @bread
    @greenery
    def filling():
        print('Ветчина')

    filling()

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    plagins = {}

    def plagin_func(func):
        def wrappend_func(*args, **kwargs):
            print('Имя функции: {name}\nИменованные аргументы {args}\nАргументы{kwargs}'.format(
                name=func.__name__, args=args, kwargs=kwargs
            ))
            plagins[func.__name__] = func
            return func
        return wrappend_func

    @plagin_func
    def timer(func):
        def wrappend_func(*args, **kwargs):
            start_func = time.time()
            func(*args, **kwargs)
            start_func = time.time()
            return
        return wrappend_func
    @plagin_func
    @timer
    def tomato():
        score = random.randint(1, 100)
        pasta = score * 70 / 100
        print('Количество пасты {pasta} получится из {score} кг помидор'.format(pasta=pasta, score=score))

    tomato()
    print(plagins)

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')


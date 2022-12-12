"""
Задача 1. Createtime
Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта
класса каждый раз, когда объект класса создаётся в основном коде.


Задача 2. Декорацию знаешь?
На новой работе вы познакомились с middle-разработчиком на Python, который согласился научить вас всему,
что умеет сам. Но перед этим он решил точечно проверить ваши знания. Он показал код, где один и тот же
декоратор логирования использовался для каждого метода класса отдельно:
Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
Логирование реализуйте на своё усмотрение:
это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
либо вывод всей этой информации в отдельный файл вместе с датой и временем.
"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    import functools
    import time
    from datetime import datetime
    from typing import Callable


    def time_cubes(cls):
        '''Декоратор выводит дату создания класса'''

        @functools.wraps(cls)
        def wrapped_cls(*args, **kwargs):
            print('Дата и время создания {}'.format(datetime.utcnow()))
            result = cls(*args, **kwargs)
            return result

        return wrapped_cls


    def timeer(func: Callable) -> Callable:
        """таймер считает время работы декоратора"""

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time() - start
            print('Время работы {}'.format(end))
            return result

        return wrapped


    def new_decorator(decorator: Callable) -> Callable:
        '''Новый декоратор
        Получает на ввод декоратор
        и применяет его ко всем функциям'''

        @functools.wraps(decorator)
        def decorate(cls):
            for i_file in dir(cls):
                if i_file.startswith('__') is False:
                    new_method = getattr(cls, i_file)
                    decorator_method = decorator(new_method)
                    setattr(cls, i_file, decorator_method)
            return cls

        return decorate


    @time_cubes
    @new_decorator(timeer)
    class Function:
        def __init__(self, numbers: int) -> None:
            self.numbers = numbers

        def cubes_sum(self) -> int:
            score = 100
            summ = 0
            for n in range(self.numbers + 1):
                summ += n ** 3 + n ** 3 + n ** 30
            print(summ)
            return summ

        def squares_sum(self, score: int):
            summ = 0
            for n in range(score + 1):
                summ += n ** 2 + n ** 2 + n ** 20
            print(summ)
            return summ


    num_1 = Function(numbers=300000)
    num_1.cubes_sum()
    num_1.squares_sum(788999)
    time.sleep(1)
    num_2 = Function(numbers=3000)
    time.sleep(1)
    num_3 = Function(numbers=3000)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    import datetime


    def logged(func):
        def wrapped(*args, **kwargs):
            print("Запуск функции произошёл в:", datetime.datetime.now())
            return func(*args, **kwargs)

        return wrapped


    def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            a = getattr(cls, i_method)
            if hasattr(a, '__call__'):
                decorated_a = logged(a)
                setattr(cls, i_method, decorated_a)
        return cls


    @decorator
    class A:

        def test_sum_1(self) -> int:
            print('Тут метод test_sum_1')
            number = 100
            result = 0
            for _ in range(number + 1):
                result += sum([i_num ** 2 for i_num in range(10000)])

            return result


    A().test_sum_1()


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

    import datetime


    def decorator(cls):
        def wrapper(*args, **kwargs):
            instance = cls(*args, **kwargs)

            print("Время создания -", datetime.datetime.now())
            print("Методы:", end=" ")
            for i_method in dir(cls):
                if i_method.startswith('__'):
                    continue
                print(i_method, end=' ')
            print()
            return instance

        return wrapper


    @decorator
    class Example:

        def hello(self):
            print("hello")

        def hello_2(self):
            print("hello")


    Example()
    Example()


else:
    print('Выберите задачу заново.')
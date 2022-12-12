"""
Задача 1. Повторение кода
В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.

Задача 2. Замедление кода 2
Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор, который перед выполнением декорируемой
функции ждёт несколько секунд.

Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
как с аргументами, так и без них.


"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    import functools
    from _collections_abc import Callable


    def new_scor(_func=None, *, scor=2):
        def scor_print(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapped_func(*args, **kwargs):
                for _ in range(scor):
                    func(*args, **kwargs)

            return wrapped_func

        return scor_print


    @new_scor(scor=3)
    def print_name(name):
        print('Привет {}'.format(name))


    my_name = print_name('Tom')


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    import time
    import functools
    from contextlib import contextmanager
    from _collections_abc import Callable


    def searh(_func=None, numbers: int = 1):
        def timer(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                print('Начало')
                start = time.time()
                for _ in range(5):
                    time.sleep(numbers)
                    func(*args, **kwargs)
                    print('Время работы {}'.format(time.time() - start))
                return func

            return wrapped

        return timer


    @searh(numbers=7)
    def scores():
        print(333 * 55 ** 33333)


    numbers = scores()


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')
"""
Задача 1. Двойной вызов
Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
Не забывайте про документацию и аннотации типов.

Пример декорируемой функции:
def greeting(name):
    print('Привет, {name}!'.format(name=name))

Основной код:
greeting('Tom')

Результат:
Привет, Tom!
Привет, Tom!

Задача 2. Таймер 2
Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию,
которая сделала всю работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете.
Однако, увидев свой код, вы как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.

Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.
"""

from typing import Callable, Any
import time
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    def do_twice(func: Callable) -> Callable:
        """Декоратор функции """
        def wrapped_func(*args, **kwargs) -> Any:
            func(*args, **kwargs)
            func(*args, **kwargs)
            func(*args, **kwargs)
            func(*args, **kwargs)
            return
        return wrapped_func

    @do_twice
    def greeting(name: str) -> None:
        print('Привет, {name}!'.format(name=name))

    greeting('Tom')

elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    print('Ханойские башни')

    def timer(func: Callable) -> Callable:
        """Декоратор"""
        def wrapped_func(*args, **kwargs) -> Any:
            """Функция подсчета времени выполнения программы"""
            start_func = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            result = round(end_time - start_func, 4)
            print('Время выполнения функции: {}'.format(result))
            return
        return wrapped_func


    def move(n: int, x: int, y: int) -> None:
        if n == 1:
            print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(x, y))
        else:
            tmp = 6 - x - y
            move(n - 1, x, tmp)
            print('Переложить диск {} со стержня номер {} на стержень номер {}'.format(n, x, y))
            move(n - 1, tmp, y)


    @timer
    def main(num: int) -> None:
        x = 1
        y = 3
        move(num, x, y)
    num = int(input('Введите количество дисков: '))
    main(num)

elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')


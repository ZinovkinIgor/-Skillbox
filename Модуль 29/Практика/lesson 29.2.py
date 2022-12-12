"""
Задача 1. Таймер
Реализуйте функцию (не класс) timer в качестве контекст-менеджера: функция должна работать с
оператором with и замерять время работы вложенного кода.

Задача 2. Директории
Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую
директорию на новую. Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок
(например, если такого пути не существует). Вне зависимости от результата выполнения контекст-менеджера
нужно возвращаться в изначальную рабочую директорию.

Пример основного кода:
with in_dir('C:\\'):
    print(os.listdir())
Результат:
<тут все папки из вашего диска C>
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    from contextlib import contextmanager
    import time

    @contextmanager
    def timer():
        start_time = time.time()
        try:
            yield
        except Exception as exp:
            print('Ошибка: {}'.format(exp))
        finally:
            print('Время работы программы: {}'.format(time.time() - start_time))


    with timer() as t1:
        var_1 = 100 * 100 ** 1000000
        print('Расчет первого числа. {}')

    with timer() as t2:
        var_1 = 200 * 200 ** 1000000
        print('Расчет первого числа. {}')

    with timer() as t3:
        var_1 = 300 * 300 ** 1000000
        print('Расчет первого числа. {}')


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')


    import os
    from contextlib import contextmanager

    @contextmanager
    def im_dir(text):
        new_dic = os.getcwd()
        print(os.listdir(text))

        try:

            yield
        except Exception as exp:
            print('Ошибка: {}'.format(exp))
        finally:
            print('{}'.format(new_dic))


    with im_dir('C:\\'):
        print(os.listdir())




elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')
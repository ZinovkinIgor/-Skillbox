"""
Задача 1. Машина
Напишите класс Toyota, состоящий из четырёх статических атрибутов:
цвет машины (например, красный),
цена (один миллион),
максимальная скорость (200),
текущая скорость (ноль).
Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

Задача 2. Однотипные объекты
В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики:
название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.
У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии микрофона.

Для внесения в базу программист начал писать такой код:
monitor_name_1 = 'Samsung'
monitor_matrix_1 = 'VA'
monitor_res_1 = 'WQHD'
monitor_freq_1 = 60
monitor_name_2 = 'Samsung'
monitor_matrix_2 = 'VA'
monitor_res_2 = 'WQHD'
monitor_freq_2 = 144
monitor_name_3 = 'Samsung'
monitor_matrix_3 = 'VA'
monitor_res_3 = 'WQHD'
monitor_freq_3 = 70
monitor_name_4 = 'Samsung'
monitor_matrix_4 = 'VA'
monitor_res_4 = 'WQHD'
monitor_freq_4 = 60

headphones_name_1 = 'Sony'
headphones_sensitivity_1 = 108
headphones_micro_1 = False
headphones_name_2 = 'Sony'
headphones_sensitivity_2 = 108
headphones_micro_2 = True
headphones_name_3 = 'Sony'
headphones_sensitivity_3 = 108
headphones_micro_3 = True

Поправьте программиста: перепишите код, используя классы и экземпляры классов.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    import random

    class MyAuto():
        color = 'Red'
        price = '1600000'
        speed_max = '220'
        speed_curron = '100'

    auto_1 = MyAuto()
    auto_1.speed_curron = random.randint(0, 200)
    auto_2 = MyAuto()
    auto_2.speed_curron = random.randint(0, 200)
    auto_3 = MyAuto()
    auto_3.speed_curron = random.randint(0, 200)
    print('{}\n{}\n{}'.format(auto_1.speed_curron, auto_2.speed_curron, auto_3.speed_curron))





elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Monitor():
        name = 'Samsung'
        matrix = 'VA'
        resolution = 'WQHD'
        frequency = '60'

    class Headphones():
        name = 'Sony'
        sensitivity = '108'
        micro = False


    monitor_1 = Monitor()
    monitor_2 = Monitor()
    monitor_3 = Monitor()
    monitor_4 = Monitor()
    monitor_2.frequency = 120
    monitor_3.frequency = 70
    print('Название: {name} \nМатрица: {matrix} \nРазрешение: {resol} \nЧастота обновления: {freq}'.format(
        name=monitor_1.name,
        matrix=monitor_1.matrix,
        resol=monitor_1.resolution,
        freq=monitor_1.frequency))
    print('\n\nНазвание: {name} \nМатрица: {matrix} \nРазрешение: {resol} \nЧастота обновления: {freq}'.format(
        name=monitor_2.name,
        matrix=monitor_2.matrix,
        resol=monitor_2.resolution,
        freq=monitor_2.frequency))
    print('\n\nНазвание: {name} \nМатрица: {matrix} \nРазрешение: {resol} \nЧастота обновления: {freq}'.format(
        name=monitor_3.name,
        matrix=monitor_3.matrix,
        resol=monitor_3.resolution,
        freq=monitor_3.frequency))
    print('\n\nНазвание: {name} \nМатрица: {matrix} \nРазрешение: {resol} \nЧастота обновления: {freq}'.format(
        name=monitor_4.name,
        matrix=monitor_4.matrix,
        resol=monitor_4.resolution,
        freq=monitor_4.frequency))

    headphones_1 = Headphones()
    headphones_2 = Headphones()
    headphones_3 = Headphones()
    headphones_2.micro = True
    headphones_3.micro = True


    print('\n\nНазвание: {name}\nЧувствительность: {sens}\nМикрофон: {micro}'.format(
        name=headphones_1.name,
        sens=headphones_1.sensitivity,
        micro=headphones_1.micro))
    print('\n\nНазвание: {name}\nЧувствительность: {sens}\nМикрофон: {micro}'.format(
        name=headphones_2.name,
        sens=headphones_2.sensitivity,
        micro=headphones_2.micro))
    print('\n\nНазвание: {name}\nЧувствительность: {sens}\nМикрофон: {micro}'.format(
        name=headphones_3.name,
        sens=headphones_3.sensitivity,
        micro=headphones_3.micro))





elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
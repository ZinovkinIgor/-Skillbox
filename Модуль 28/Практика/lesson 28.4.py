"""
Задача 1. Транспорт
У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
В парке транспорта стоят:

Автомобили. Они могут ездить только по земле.
Лодки. Ездят только по воде.
Амфибии. Могут перемещаться и по земле, и по воде.
Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным
и содержать абстрактные методы.
Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»

Задача 2. Фигуры
При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты.
Каждая из них имеет координаты XY, длину и ширину. Также каждая фигура может менять координаты (двигаться) и менять размер.
Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат —
это разные фигуры и работают они по-разному. В частности, по разному работает метод изменения размера фигуры,
 так как у квадрата все стороны равны.
"""
import random

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    class Transport:
        """Создаем родительский класс, указываем цвет, скорость, метод подача сигнала, движение вперед"""
        def __init__(self):
            self.color = 'Black'
            self.speed = 20

        def signal(self):
            print('Подача сигнала. Биб.')

        def movement(self, hight):
            print('Едет по дороге {} метров'.format(hight))

    class Chip(Transport):
        def __init__(self):
            super().__init__()
            self.name = 'Лодка'

        def movement(self, hight):
            print('Плывет по реке {} метров'.format(hight))

    class Auto(Transport):
        def __init__(self):
            super().__init__()
            self.name = 'Автомобиль'

    class Amphibian(Transport):
        def __init__(self):
            super().__init__()
            self.name = 'Амфибия'

        def movement(self, hight):
            print('Плывет по реке и едет по дороге {} метров'.format(hight))

    """Запускаем программу и выводим все на экран"""
    tur_1 = Auto()
    tur_2 = Amphibian()
    tur_3 = Chip()
    for tur in (tur_1, tur_2, tur_3):
        print('Вид транспорта: {name}, цвет - {color}, скорость движения - {speed}'.format(
            name=tur.name, color=tur.color, speed=tur.speed
        ))
        tur.movement(random.randint(100, 900))
        tur.signal()


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Figure:
        def __init__(self, x, y, length, width):
            self.x = x
            self.y = y
            self.lenght = length
            self.width = width

        def info_print(self):
            print('Координаты точки х={x} , у={y} , длинна={len} , ширина={wid}'.format(
                x=self.x, y=self.y, len=self.lenght, wid=self.width
            ))

    class Rectangle(Figure):
        def __init__(self, x, y, length, width):
            super().__init__(x, y, length, width)

    class Square(Figure):
        def __init__(self, x, y, length):
            super().__init__(x, y, length, length)

    figure_1 = Rectangle(2, 5, 8, 5)
    figure_2 = Square(4, 6, 9)
    figure_1.info_print()
    figure_2.info_print()





elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')











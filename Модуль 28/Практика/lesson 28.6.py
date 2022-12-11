"""Задача 1. Транспорт 2
Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и сеттерами
для соответствующих атрибутов. Используйте встроенные декораторы. Вот входные данные той задачи:

У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
В парке транспорта стоят:

Автомобили. Они могут ездить только по земле.
Лодки. Ездят только по воде.
Амфибии. Могут перемещаться и по земле, и по воде.
"""

from abc import ABC


class Transport(ABC):
    '''
    Родительский класс транспорта
    общее цвет, скорость. подача сигнала, движение
    '''

    def __init__(self, color: str, speed: int, signal: bool = False):
        self.color = color
        self.speed = speed
        self.signal = signal
        self.movement = None

    def drive(self, coord_x=0, coord_y=0) -> None:
        '''Движение по земле'''
        self.coord_x = coord_x
        self.coord_x = coord_y

    def to_sail(self, coord_x=0, coord_y=0) -> None:
        '''Движение по воде'''
        self.coord_x = coord_x
        self.coord_x = coord_y


class Music:
    '''Играет музыка'''
    pass


class Car(Transport, Music):
    '''Автомобиль ездит по дороге, слушает музыку, может подавать сигнал'''

    def __init__(self, color: str, speed: int) -> None:
        super().__init__(color, speed)
        self.drive(4, 4)



class A_boat(Transport, Music):
    '''Катер плывет по реке, слушает музыку, может подавать сигнал'''

    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.to_sail()


class Amphibian(Transport, Music):
    '''Амфибия ездит по дороге и плывет по реке, слушает музыку, может подавать сигнал'''

    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.drive()
        self.to_sail()


auto_1 = Car(color='blue', speed=200)
print(auto_1.color, auto_1.speed, )

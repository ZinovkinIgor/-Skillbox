"""
Задача 1. Юниты
Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие «получить урон»
(базовый класс получает 0 урона).

Также есть два дочерних класса:
Солдат: получает урон, равный переданному значению.
Обычный гражданин: получает урон, равный двукратному переданному значению.
Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма
(а также инкапсуляции и наследования, конечно же).
"""

"""
Задача 2. Полёт
Иногда для реализации дочерних классов используется так называемый класс-роль, где также описываются
общие атрибуты и методы, но в программе инициализируются объекты только дочерних классов,
а базовый класс-роль не трогается. К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться.

Реализуйте класс «Может летать».
Атрибуты:
Высота = 0.
Скорость = 0.
Методы:

Взлететь (в теле прописать pass).
Лететь (в теле прописать pass).
Приземлиться (установить высоту и скорость в значение 0).
Вывести высоту и скорость на экран.

Затем реализуйте два дочерних класса:

«Бабочка», который может:
Взлететь (высота = 1).
Лететь (скорость = 0.5).

«Ракета», которая может:
Взлететь (высота = 500, скорость = 1000).
Приземлиться (высота = 0, взрыв).
Взорваться (тут уже что угодно).
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)


    class Unit:
        '''
        Создали родительский класс
        урон здоровья
        '''

        def __init__(self, health=0, damage=0):
            self.health = health
            self.damage = damage

        def __str__(self):
            self.health -= self.damage
            return 'Нападение на война, {} урон. Осталось здоровья {}'.format(
                self.damage, self.health
            )

    class Voin(Unit):
        """
        Определяем война, с родительского класса, ставим здоровье и урон
        """

        def __init__(self, health, damage):
            super().__init__(health)
            self.damage = damage


    class Peasant(Unit):
        """
        Определяем гражданина, с родительского класса, ставим здоровье и урон
        переопределяем урон здоровья
        """

        def __init__(self, health, damage):
            super().__init__(health)
            self.damage = damage

        def __str__(self):
            self.health -= self.damage * 2
            return 'Нападение на гражданина, {} урон. Осталось здоровья {}'.format(
                self.damage, self.health
            )

    voin = Voin(100, 5)
    print(voin)
    peas = Peasant(100, 5)
    print(peas)


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Flight:
        """
        Класс полет. Определяем высоту и скорость.
        """
        def __init__(self, name, hight, speed):
            self.name = name
            self.hight = hight
            self.speed = speed

        def __str__(self):
            return "{} летит на юг.".format(self.name)

        def take_off(self):
            """
            Класс взлететь.
            """
            pass

        def fly(self):
            """
            Класс лететь.
            """
            pass

        def land(self):
            """
            Класс приземлиться. Скорость 0, высота 0
            """
            self.hight = 0
            self.speed = 0


        def info_print(self):
            print('Летит на высоте {} со скоростью {}'.format(self.hight, self.speed))


    class Butterfly(Flight):
        def __init__(self, name, hight, speed):
            super().__init__(name, hight, speed)


    class Rocket(Flight):
        def __init__(self, name, hight, speed, fall,):
            super().__init__(name, hight, speed)
            self.fall = fall



        def land(self):
            self.hight -= self.fall
            if self.hight <= 0:
                return 'Взрыв'
            else:
                return 'Ракета снижается'


    batt = Butterfly(name="JJJ", hight=1, speed=0.5)
    print(batt)
    batt.info_print()
    rocketa = Rocket(name='SATANA', hight=1000, speed=790, fall=500)
    print(rocketa)
    rocketa.info_print()
    print(rocketa.land())
    print(rocketa.land())


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
"""
Задача 1. Координаты точки
В одной из практик предыдущего модуля была задача на реализацию класса «Точка». Модернизируйте класс по следующему условию:
объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут передаваться пользовательские значения
координат, по умолчанию x = 0, y = 0.

Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
Предоставление информации о точке (используйте магический метод str).
Геттер и сеттер для x.
Геттер и сеттер для y.
Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.

Задача 2. Человек
Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом
(должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов.
Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения и
получения данных объекта напишите специальные геттеры и сеттеры.

При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и «крайне не
рекомендуемым», который был показан в уроке.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)

    class Point:
        __min_point = -100
        __max_point = 100

        def __init__(self, x=0, y=0):
            self.set_coordinat_x(x)
            self.set_coordinat_y(y)

        def __str__(self):
            return 'Точка x={}; y={}'.format(self.__x, self.__y)

        def get_coordinate_x(self):
            return self.__x

        def get_coordinate_y(self):
            return self.__y

        def set_coordinat_x(self, x):
            if x in range(self.__min_point - 1, self.__max_point + 1):
                self.__x = x
            else:
                raise ValueError('Вы вышли за диапазон')

        def set_coordinat_y(self, y):
            if y in range(self.__min_point - 1, self.__max_point + 1):
                self.__y = y
            else:
                raise ValueError('Вы вышли за диапазон')

    coor_z = Point()
    coor_z.set_coordinat_x(98)
    coor_z.set_coordinat_y(9)
    print(coor_z)
    print(coor_z.get_coordinate_x())


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Person:
        __min_age = 0
        __max_age = 100

        def __init__(self, name='Рома', age=29):
            self.__name = name
            self.__age = age

        def __str__(self):
            return 'Имя: {}\nВозраст: {}'.format(self.__name, self.__age)

        def get_name(self):
            return self.__name

        def get_age(self):
            return self.__age

        def set_name(self, name):
            if name.isalpha():
                self.__name = name
            else:
                raise NameError('Ошибка имени, имя должно содержать только буквы')

        def set_age(self, age):
            if age in range(self.__min_age - 1, self.__max_age + 1):
                self.__age = age
            else:
                raise NameError('Ошибка возраста. Вы вышли за диапазон')

    human = Person('Игорь', 34)
    print(human)
    human.set_age(36)
    print(human.get_age())
    human.set_name('fff')
    print(human.get_name())



elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')
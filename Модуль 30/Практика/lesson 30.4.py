"""
Задача 1. Минимум и максимум
Мы знаем, что для нахождения минимального и максимального значений в наборе данных можно использовать две
встроенные функции: min() и max(). И у них тоже можно использовать именованный аргумент key.



Скажем, дан вот такой список, в котором хранятся результаты соревнований в виде словарей:

grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
{'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44},
{'name': 'Jana', 'score': 45},

{'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},

{'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},

{'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},

{'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},

{'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},

{'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},

{'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},

]

Напишите код, который выводит на экран минимальное и максимальное количество очков из этого списка.
 Используйте только встроенные функции и лямбда-функции, то есть реализуйте решение «в две строки».

Задача 2. Сортировка
Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке: его имя,
возраст и остальные данные. Вас попросили реализовать для этой базы сортировку по возрасту
(по убыванию и по возрастанию).

Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.
"""

task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))
if task == 1:
    # Задача 1
    print('=' * 40)

    from typing import Dict, Union

    grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
                                          {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37},
                                          {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
                                          {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2},
                                          {'name': 'Mary', 'score': 63},
                                          {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44},
                                          {'name': 'Richard', 'score': 78},
                                          {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13},
                                          {'name': 'Lloyd', 'score': 52},
                                          {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40},
                                          {'name': 'James', 'score': 54},
                                          {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9},
                                          {'name': 'Bruce', 'score': 68},
                                          {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22},
                                          {'name': 'Aaron', 'score': 3},
                                          {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94},
                                          {'name': 'Sandra', 'score': 40},
                                          ]

    print(min(grades, key=lambda res: res['score']))
    print(max(grades, key=lambda res: res['score']))


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    class Person:
        def __init__(self, name, age, date):
            self._name = name
            self._age = age
            self._date = date


        @property
        def name(self):
            return self._name

        @property
        def age(self):
            return self._age

        @property
        def date(self):
            return self._date

        @name.setter
        def name(self, name: str):
            self._name = name

        @age.setter
        def age(self, age: int):
            self._age = age

        @date.setter
        def date(self, date: str):
            self._date.append(date)

        def __repr__(self):
            return f"({self.name}, {self.age}, {self._date})"



    human_1 = Person('Иван', 34, 'ПК')
    human_2 = Person('Настя', 24, 'Спорт')
    human_3 = Person('Юля', 19, 'Фитнесс')
    human = [human_1, human_2, human_3]

    print(human)
    human.sort(key=lambda age: age.age)
    print(human)
    human.sort(key=lambda age: -age.age)
    print(human)



elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')


else:
    print('Выберите задачу заново.')
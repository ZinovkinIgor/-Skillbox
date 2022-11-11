"""
Задача 4. Отцы, матери и дети
Что нужно сделать
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
Имя.
Возраст.
Список детей.
И он может:
Сообщить информацию о себе.
Успокоить ребёнка.
Покормить ребёнка.
У ребёнка есть:
Имя.
Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
Состояние спокойствия.
Состояние голода.
Реализация состояний на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.
"""

import random


class Parents:
    '''класс родители'''
    def __init__(self, name, age):
        '''Инкапсуляция родители'''
        self.name = name
        self.age = age
        self.list_children = []


    def info_yourself(self):
        '''Информация о себе'''
        print('Расскажите немного о себе.')
        score_kids = int(input('Сколько у Вас детей: '))
        for _ in range(score_kids):
            self.name_kids = input('Как зовут ребенка: ')
            self.list_children.append(self.name_kids)
            self.age_kids = int(input('Сколько лет ребенку: '))
            kids = Children(self.name_kids, self.age_kids)
            kids.print_kids()


    def calm_baby(self, name_kids, calmness):
        '''Успокоить ребенка'''
        if calmness == 'Кричит':
            print('{} {} уго отвлекли другой игрой.'.format(name_kids, calmness))
        elif calmness == 'Плачет':
            print('{} {} уго успокоили.'.format(name_kids, calmness))
        else:
            print('{} {} всё хорошо.'.format(name_kids, calmness))

    def feed_baby(self, name_kids, hunger):
        '''Покормить ребенка'''
        if hunger == 'Голоден':
            print('{} {}  ему, дали яблоко.'.format(name_kids, hunger))
        elif hunger == 'Очень голоден':
            print('{} {} ему, дали суп.'.format(name_kids, hunger))
        else:
            print('{} {} всё хорошо.'.format(name_kids, hunger))

    def print_adult(self):
        '''Вывод на экран информацию про родителей:'''
        print('\n\nРодитель:\nИмя {}\nВозраст {}\nДети {}'.format(
            self.name, self.age, self.list_children
            )
        )

class Children:
    '''класс дети'''
    state_hunger = {0: 'Не голоден', 1: 'Наелся', 2: 'Ест', 3: 'Голоден', 4: 'Очень голоден'}
    state_calmness ={0: 'Спит', 1: 'Бегает', 2: 'Кричит', 3: 'Играет', 4: 'Плачет'}


    def __init__(self, name, age):
        '''Инкапсуляция дети'''
        self.name_kids = name
        self.age = self.age_verification(age)
        self.calmness = self.state_calmness[random.randint(0, 4)]
        self.hunger = self.state_hunger[random.randint(0, 4)]

    def print_kids(self):
        '''Вывод всего на экран'''
        adult.calm_baby(self.name_kids, self.calmness)
        adult.feed_baby(self.name_kids, self.hunger)
        adult.print_adult()


    def age_verification(self, age):
        '''Проверка возраста ребенка. не менее 16 лет разницы.'''
        while True:
            if adult.age - age >= 16:
                return age
            else:
                age = int(input('Введите возраст ребенка, раздница должна быть более 16 лет: '))


adult = Parents('Nik', 30)
adult.info_yourself()




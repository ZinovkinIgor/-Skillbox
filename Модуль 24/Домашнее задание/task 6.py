"""
Задача 6. Магия
Что нужно сделать
Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые:
«Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Вот таблица преобразований:
Вода + Воздух = Шторм
Вода + Огонь = Пар
Вода + Земля = Грязь
Воздух + Огонь = Молния
Воздух + Земля = Пыль
Огонь + Земля = Лава
Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None.
Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:

class Example_1:
    def __add__(self, other):
        return Example_2()

class Example_2:
    answer = 'сложили два класса и вывели'

a = Example_1()
b = Example_2()
c = a + b
print(c.answer)

Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.
Что оценивается
"""
'''
Создаем классы для вывода заклинаний
Запускаем цикл для создания заклинаний
'''

class Water:
    '''Элемент воды'''
    def __add__(self, magic):
        if magic == 'b':
            return 'Шторм'
        elif magic == 'c':
            return 'Пар'
        elif magic == 'd':
            return 'Грязь'
        elif magic == 'e':
            return 'Ледяной шип'
        elif magic == 'f':
            return 'Ливень'
        else:
            return None

class Air:
    '''Элемент воздуха'''
    def __add__(self, magic):
        if magic == 'a':
            return 'Шторм'
        elif magic == 'c':
            return 'Молния'
        elif magic == 'd':
            return 'Пыль'
        elif magic == 'e':
            return 'Метель'
        elif magic == 'f':
            return 'Ураган'
        else:
            return None

class Fire:
    '''Элемент огня'''
    def __add__(self, magic):
        if magic == 'a':
            return 'Пар'
        elif magic == 'b':
            return 'Молния'
        elif magic == 'd':
            return 'Лава'
        elif magic == 'e':
            return 'Взрыв'
        elif magic == 'f':
            return 'Шаровая молния'
        else:
            return None

class Earth:
    '''Элемент земли'''
    def __add__(self, magic):
        if magic == 'a':
            return 'Грязь'
        elif magic == 'b':
            return 'Пыль'
        elif magic == 'c':
            return 'Лава'
        elif magic == 'e':
            return 'Камень'
        elif magic == 'f':
            return 'Песчаный удар'
        else:
            return None

class Frost:
    '''Мороз'''
    def __add__(self, magic):
        if magic == 'a':
            return 'Ледяной шип'
        elif magic == 'b':
            return 'Метель'
        elif magic == 'c':
            return 'Взрыв'
        elif magic == 'd':
            return 'Камень'
        elif magic == 'f':
            return 'Морозная стена'
        else:
            return None

class Wind:
    '''Ветер'''
    def __add__(self, magic):
        if magic == 'a':
            return 'Ливень'
        elif magic == 'b':
            return 'Ураган'
        elif magic == 'c':
            return 'Шаровая молния'
        elif magic == 'd':
            return 'Песчаный удар'
        elif magic == 'e':
            return 'Морозная стена'
        else:
            return None


class Magic_spell:
    """
    Создаем словарь с названиями заклинаний
    Вводим заклинания с клавиатуры
    Выводим на экран и вызываем определенный клас заклинания + передаем 2 заклинание
    """

    spells_list = {'a': 'Вода', 'b': 'Воздух', 'c': 'Огонь', 'd': 'Земля', 'e': 'Мороз', 'f': 'Ветер'}
    def __init__(self):
        print('Решение 2 способом\na - Вода \nb - Воздух\nc - Огонь\nd - Земля\ne - Мороз\nf - Ветер\n')
        self.spell_1 = input('Выберите первое заклинание: ')
        self.spell_2 = input('Выберите второе заклинание: ')

    def spell(self, spell_2):
        if self.spell_1 == 'a':
            return Water() + spell_2
        elif self.spell_1 == 'b':
            return Air() + spell_2
        elif self.spell_1 == 'c':
            return Fire() + spell_2
        elif self.spell_1 == 'd':
            return Earth() + spell_2
        elif self.spell_1 == 'e':
            return Frost() + spell_2
        elif self.spell_1 == 'f':
            return Wind() + spell_2

    def print_spell(self):
        print('{} + {} = {}'.format(self.spells_list[self.spell_1], self.spells_list[self.spell_2], self.spell(self.spell_2)))

while True:
    spell_atak = Magic_spell()
    spell_atak.print_spell()

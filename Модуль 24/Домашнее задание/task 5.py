"""
Задача 5. Весёлая ферма 2
Что нужно сделать
Мы продолжаем писать игру «Весёлая ферма», и теперь необходимо её немного модернизировать. Всё-таки кому-то нужно
собирать урожай, и для этого нам понадобится садовник, у которого есть:
Имя.
Грядка с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
И он может:
Ухаживать за грядкой.
Собирать с неё урожай (количество картошки ― пустой список).
Модернизируйте программу, используя новый класс «Садовник». На всякий случай даём описание картошки и грядки:
У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и расти.
Всего у картошки может быть четыре стадии зрелости.
Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
а также предоставлять информацию о зрелости всей картошки на своей территории.

Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку садовнику. Пусть поухаживает за грядкой
и соберёт урожай (а может быть даже и не один).
"""

import random
# класс садовник
# атрибуты (Имя, Грядки, Урожай)
# методы (уход за урожаем, сбор урожая)

class Gardener:
    """
    Садовник получает данные, имя, сколько грядок, количество дней.
    У него есть методы: ухода за урожаем в случае погодных условий и сбор урожая
    """
    def __init__(self, name, scor, day):
        self.name = name
        self.all_beds = Garden(scor).new_garden_dict
        self.harvest = {(name[0], name[1]): 0 for name in self.all_beds.items()}
        self.day = day
        self.harvesting(day)
        self.print_info()

    # метод уход за урожаем
    def crop_care(self):
        pass

    # метод сбор урожая
    def harvesting(self, day):
        """
        запускаем цикл по дням и каждый день проходим по каждой грядке и выводим результат созревания
        """
        for day_num in range(1, day + 1):
            print('\nНачался день {}. '.format(day_num))
            for key, value in self.harvest.items():
                number = Vegetables(key, value, day_num)
                self.harvest[key] += number.summ



    # Вывод на экран всех данных
    def print_info(self):
        print('\n\nВывод результата на экран Имя садовника: {}\nСписок грядок: {}\nВесь урожай за все время: {}'.format(
            self.name,
            self.all_beds,
            self.harvest))

# Грядка. определяет что растет
class Garden:
    garden = ['Картошка']
    # garden = [
    #     'Картошка',
    #     'Помидоры',
    #     'Огурцы',
    #     'Редис',
    #     'Лук']

    def __init__(self, scor):
        self.scor = scor
        self.filling_beds()

    # заполнение грядок
    def filling_beds(self):
        self.new_garden_dict = dict()
        self.new_garden = [random.choice(Garden.garden) for _ in range(self.scor)]
        for num, name in enumerate(self.new_garden):
            self.new_garden_dict[num + 1] = name
        return self.new_garden_dict

# Овощи, как растут.
class Vegetables:

    potato_ripening = {
        1: 'посадка',
        2: 'прорастание',
        3: 'Нарастание вегетативной массы',
        4: 'бутонизация',
        5: 'цветение',
        6: 'созревание',
        7: 'увядание',
        8: 'вся грядка созрела'}

    def __init__(self, key, value, day_num):
        self.day = day_num
        self.num_gard = key
        self.name = value
        self.summ = 0
        self.yield_season = 100
        self.there_growth()



    def there_growth(self):
        """
        Выводим на экран стадию созревания грядки.
        Если грядка созрела, то начинается посадка заново. Пока идет срок игры.
        """
        day = 0
        if self.day > len(Vegetables.potato_ripening):
            day = (self.day % len(Vegetables.potato_ripening)) + 1
            self.summ += self.yield_season

        else:
            day = self.day

        print('Грядка № {} с {} в стадии {}'.format(
            self.num_gard[0],
            self.num_gard[1],
            Vegetables.potato_ripening[day]))
        return self.summ

# погодные условия
class Weather:
    weather_conditions = {
        0: 'Светит солнце',
        1: 'Идет дождь',
        2: 'Ураган',
        3: 'Жара',
        4: 'Заморозки',
        5: 'Проливные дожди'}

    # Светит солнце
    def sun_shining(self):
        pass

    # Идет дождь
    def rain(self):
        pass

    # Ураган
    def hurricane(self):
        pass

    # Жара
    def heat(self):
        pass

    # Заморозки
    def frost(self):
        pass

    # Проливные дожди,
    def torrential_rains(self):
        pass

farmer = Gardener('Tod', 4, 99)






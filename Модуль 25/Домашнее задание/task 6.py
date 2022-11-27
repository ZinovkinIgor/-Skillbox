"""
Задача 6. Совместное проживание 2
Что нужно сделать

Артём увлёкся предыдущим экспериментом и решил расширить его, создав целую семью из Мужа, Жены и Кота.
Условия эксперимента следующие.
Каждый день участники жизни могут делать только одно действие. Все вместе они должны прожить год и не умереть.

Муж может:
есть;
играть;
ходить на работу.

Жена может:
есть;
покупать продукты;
покупать шубу;
убираться в доме.

Кот может:
есть;
спать;
драть обои.

Все они живут в одном доме, дом характеризуется:
  количеством денег в тумбочке (вначале 100);
  количеством еды в холодильнике (вначале 50);
  едой для кота (вначале 30);
  количеством грязи (вначале 0).

У людей есть имя, степень сытости (вначале 30) и степень счастья (вначале 100). Все люди могут гладить кота (+5 к счастью).
У кота есть имя и степень сытости (вначале 30).

Любое действие (в том числе и кота), кроме «есть», приводит к уменьшению степени сытости на 10 пунктов.
Взрослые едят максимум по 30 единиц еды, степень сытости растёт на один пункт за один пункт еды.
Кот ест максимум по 10 единиц еды, степень сытости растёт на два пункта за один пункт еды.
Степень сытости не должна падать ниже нуля, иначе человек или кот умрёт от голода.
Деньги в тумбочку добавляет муж после работы — сразу 150 единиц.
Еда стоит 10 денег за 10 единиц еды. Шуба стоит 350 единиц.
Еда для кота тоже покупается — за 10 денег 10 еды.
Грязь добавляется каждый день по пять пунктов, за одну уборку жена может убирать до 100 единиц грязи.
Если кот дерёт обои, то грязи тоже становится больше на пять пунктов.
Если в доме грязи больше 90, у людей падает степень счастья каждый день на 10 пунктов.
Степень счастья растёт: у мужа от игры в компьютер (на 20), у жены от покупки шубы (на 60, но шуба дорогая).
Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.

Реализуйте такую программу. Подведите итоги жизни за год — сколько было заработано денег, сколько съедено еды,
сколько куплено шуб.
Дополнительно: добавьте ещё ребёнка и несколько котов.
"""

import random

class Human:
    '''
    Добавляем человека
    __name - имя
    __satiety - сытость = 30
    __happiness - счастье = 100
    '''
    def __init__(self, name, satiety=30, happiness=100):
        self.__name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        '''поесть + 30 сытость, - 30 еда в холодильнике'''
        self.satiety += 30
        House.meal_human -= 30

    def petting_cat(self):
        self.happiness += 5
        self.satiety -= 10



class Animal:
    '''
    Добавляем кота
    __name - имя
    satiety - сытость = 30
    '''
    def __init__(self, name, satiety = 30):
        self.__name = name
        self.satiety = satiety

    def eat(self):
        '''поесть + 30 сытость, - 30 еда в холодильнике'''
        self.satiety += 20
        House.meal_cat -= 10
        print('Кот ест')




class Husband(Human):
    '''
    plays_computer - играет в компьютер: - 10 сытость, + 20 счастья
    goes_work - ходит на работу:  - 10 сытость, + 150 денег
    '''
    def plays_computer(self): # Играет в компьютер, но если нет денег то идет работать
        if House.money < 100:
            self.goes_work()
        else:
            self.satiety -= 10
            self.happiness += 20
            print('Играет в компьютер')

    def goes_work(self): # работает
        self.satiety -= 10
        House.money += 150
        House.amount_of_money += 150 # отчет деньги за год
        print('Муж работает.')


class Wife(Human):
    '''
    buys groceries - покупает продукты: - 10 сытость, - 30 денег, + 30 еды для людей, - 10 денег, + 20 еды для кота
    buys a fur coat - покупает шубу: - 10 сытость, - 350 денег, + 60 счастья
    cleans the house - убирает в доме: - 10 сытость, до - 100 грязь в доме
    '''
    def eat(self):
        '''поесть + 30 сытость, - 30 еда в холодильнике'''
        if House.meal_human < 50: # если нет продуктов
            self.buys_groceries()
        else:
            self.satiety += 30
            House.meal_human -= 30

    def buys_groceries(self):
        '''покупаем продукты'''
        if House.money > 100:
            self.satiety -= 10
            House.money -= 100
            House.meal_human += 100
            House.food_ear += 100
        elif House.money > 50:
            self.satiety -= 10
            House.money -= 50
            House.meal_human += 50
            House.food_ear += 50
        else:
            House.meal_human += House.money
            House.money = 0
        print('Жена покупает продукты.')



    def buys_groceries_cat(self):
        if House.meal_cat >= 20:
            House.money -= 10
            House.meal_cat += 20
            House.food_ear_cat += 20  # отчет еда за год
            print('Жена покупает корм.')
        else:
            House.meal_cat += House.money * 2
            print('На корм денег нет.')
            House.money = 0

    def buys_a_fur_coat(self):
        '''покупаем шубу'''
        if House.money >= 350:
            self.satiety -= 10
            House.money -= 350
            self.happiness += 60
            House.fur_coat += 1 # отчет - покупка шубы
            print('Жена покупает шубу.')
        else:
            print('На шубу денег нет.')

    def cleans_the_house(self):
        '''уборка в доме'''
        if House.dirt_house >= 100:
            self.satiety -= 10
            House.dirt_house -= 100
        elif House.dirt_house <= 100:
            self.satiety -= 10
            House.dirt_house = 0
        print('Жена убирает.')


class Cat(Animal):
    '''
    sleeping - спит - 10 сытость
    tear up wallpaper - дерет обои - 10 сытость, + 5 грязь в доме
    '''
    def sleeping(self):
        '''кот спит'''
        self.satiety -= 10
        print('Кот спит.')

    def tear_up_wallpaper(self):
        '''кот дерет обои'''
        self.satiety -= 10
        House.dirt_house += 5
        print('Кот дерет обои.')


class House:
    '''
    money - денег в тумбочке = 100
    meal_human - еды в холодильнике для человека = 50
    meal_cat - еды в холодильнике для кота = 50
    dirt_house - грязь в доме = 0
    amount_of_money - отчет за год денег
    food_ear - еды за год
    '''
    money = 100
    meal_human = 50
    meal_cat = 50
    dirt_house = 0
    amount_of_money = 0
    food_ear = 0
    fur_coat = 0
    food_ear_cat = 0

    def life_husband(self):
        if husband.satiety <= 10:
            husband.eat()
        elif husband.happiness <= 10:
            husband.plays_computer()
        else:
            numbers = random.randint(1, 4)
            if numbers == 1:
                husband.plays_computer()
            elif numbers == 2:
                husband.goes_work()
            elif numbers == 3:
                husband.eat()
                print('Муж ест.')
            elif numbers == 4:
                husband.petting_cat()
                print('Муж гладит кота')
        print('Счастья {}, сытость {}'.format(husband.happiness, husband.satiety))

    def life_wile(self):
        if wife.satiety < 20: # сытость меньше 10, ест
            wife.eat()
        elif House.meal_human < 50: # еды меньше 30 идет в магазин
            wife.buys_groceries()
        elif House.meal_cat < 50: #корма меньше 50 идет в магазин
            wife.buys_groceries_cat()
        elif wife.happiness <= 20 and House.money > 500: # если мало счастья и много денег, то купить шубу
            wife.buys_a_fur_coat()
        elif wife.happiness <= 40: #если мало счастья гладить кошку
            wife.petting_cat()
        elif House.dirt_house > 50: # если грязно в доме
            wife.cleans_the_house()
        else:                       # рандомно выбирается действие
            numbers = random.randint(1, 5)
            if numbers == 1:
                wife.buys_a_fur_coat()
            elif numbers == 2:
                wife.cleans_the_house()
            elif numbers == 3:
                wife.eat()
                print('Жена ест.')
            elif numbers == 4:
                wife.buys_groceries()
            elif numbers == 5:
                wife.petting_cat()
                print('Жена гладит кота')
        print('Счастья {}, сытость {}'.format(wife.happiness, wife.satiety))


    def life_cat(self):
        if cat.satiety <= 10:
            cat.eat()
        else:
            numbers = random.randint(1, 3)
            if numbers == 1:
                cat.eat()
            elif numbers == 2:
                cat.sleeping()
            elif numbers == 3:
                cat.tear_up_wallpaper()

    def day(self):
        '''
        прошел день: грязь в доме + 5
        сразу проверка, если в доме >=  90 грязи то у всех - 10 счастья
        '''
        House.dirt_house += 5
        if House.dirt_house >= 90:
            husband.happiness -= 10
            wife.happiness -= 10

    def death(self):
        '''
        проверка сытость если <= 0 - то смерть от голода,  и счастье если меньше 10 - то смерть от дипрессии
        '''
        if husband.satiety <= 0:
            raise ('Муж умер от голода.')
        elif wife.satiety <= 0:
            raise ('Жена умерла от голода.')
        elif cat.satiety <= 0:
            raise ('Кот умер от голода.')
        elif husband.happiness < 10:
            raise ('Муж умер от дипрессии.')
        elif wife.happiness < 10:
            raise ('Жена умерла от дипресии.')


husband = Husband(input('Введите имя мужа: '))
wife = Wife(input('введите имя жены: '))
cat = Cat(input('Введите кличку кота: '))
home = House()
numbers = int(input('Введите сколько дней нужно прожить: '))
for day in range(1, numbers + 1):
    print('\nДень {}\nДенег в семье: {}\nЕды в холодильнике: {}\nКорм кота: {}\nГрязи в доме: {}'.format(
        day, home.money, home.meal_human, home.meal_cat, home.dirt_house
    ))
    home.death()
    home.day()
    home.life_husband()
    home.life_wile()
    home.life_cat()
print('Отчет за год:\nЗаработано денег за год: {},\nКуплено еды в году: {},'
      '\nКуплено корма в году: {}, \nКуплено шуб в году: {}'.format(
    home.amount_of_money, home.food_ear,home.food_ear_cat, home.fur_coat
    ))
"""
Задача 1. Драка
Что нужно сделать
Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:
Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков.
Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. У того, кого бьют,
оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой юнит
атаковал и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья,
программа завершается сообщением о том, кто одержал победу.
Реализуйте такую программу.
"""

import random

class Unit:
    count = 1

    def __init__(self, name):
        self.name = name
        voin_dict[name] = 1000


    def damage(self, names):
        Unit.count += 1
        hit = random.randint(0, 20)
        voin_dict[names] -= hit
        if voin_dict[names] < 0:
            voin_dict[names] = 0

        print('По {name} наносят удар с силой {hit}. Осталось здоровья {hpp}\n'.format(
            name=self.name,
            hit=hit,
            hpp=voin_dict[names]))

        if voin_dict[names] <= 0:
            print('Воин {} проиграл.'.format(self.name))




class Battle:
    # Записываем два война
    def __init__(self, name_1, name_2):
        self.name_1 = Unit(name_1)
        self.name_2 = Unit(name_2)

        self.motion()

    def motion(self):
        while voin_dict[self.name_1.name] > 0 and voin_dict[self.name_2.name] > 0:
            self.hit()
        else:
            print('Здоровье {} осталось: {} \nЗдоровье {} осталось: {}\n'.format(
                self.name_1.name,
                voin_dict[self.name_1.name],
                self.name_2.name,
                voin_dict[self.name_2.name]))

    # рандомно выбираем атакующего
    def hit(self):
        print('{} - раунд.'.format(Unit.count))
        attaking = random.choice([self.name_1.name, self.name_2.name])
        if attaking == self.name_1.name:
            print('Удар наносит {}'.format(attaking))
            self.name_2.damage(self.name_2.name)
        else:
            print('Удар наносит {}'.format(attaking))
            self.name_1.damage(self.name_1.name)

voin_dict = dict()
Battle('Bob', 'Teddi')





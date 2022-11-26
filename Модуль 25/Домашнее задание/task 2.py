"""
Задача 2. Карма
Что нужно сделать

Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и
может с вероятностью 1 к 10 выкинуть одно из исключений:

KillError;
DrunkError;
CarCrashError;
GluttonyError;
DepressionError.
Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при
накоплении кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.
"""


import random

class LifeSimulator:
    """
    класс симулятор жизни
    args:
        day - определяет день
        :rtype int
        karma - карма накопительная
        :rtype int
        max_karma - максимальная карма которую необходимо набрать
        :rtype int
        error_list -  список всех вызываемых ошибок
        :rtype list(str)
    method:
        life - запускает цикл с проверкой будет ошибка или нет.
        Если есть ошибка вызываем исключение и записываем результат в файл error.log
        Если нет ошибок то вызываем метод life_scor  для добавления кармы
    """
    day = 0
    karma = 0
    max_karma = 500
    error_list = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']

    def life(self):
        """
        Метод life запускает цикл для накопления кармы, пока карма накопительная будет меньше максимальной кармы,
        то цикл будет выполнятся. При каждом повторении цикла, добавляется 1 день.
        args:
            count - рандомное число выбирает действие, если 1 то выдает рандомную ошибку, иначе добавляет карму.
            :rtype int
            self.random_error - рандомная ошибка из списка ошибок
            :rtype str
            report - запись в error.log
            :rtype str
        """
        while self.karma <= self.max_karma:
            self.day += 1
            count = random.randint(1, 10)
            if count == 1:
                try:
                    self.random_error = random.choice(self.error_list)
                    raise Exception(self.random_error)
                except Exception:
                    result_error = open('error.log', 'a', encoding='utf-8')
                    report = ('В {day} день вышла ошибка {err}\n'.format(day=self.day, err=self.random_error))
                    result_error.write(report)
                    result_error.close()
            else:
                self.life_scor()

    def life_scor(self):
        """
        Метод life_scor - выводит на экран день и карма за день, общая карма.
        добавляет дневную карму к накопительной.
        score_carma - рандомная карма от 1 до 7
        :rtype int
        """
        score_carma = random.randint(1, 7)
        print('В {day} день начислено кармы: {sc_karma}'.format(day=self.day, sc_karma=score_carma))
        self.karma += score_carma
        print('Общая карма {karma}'.format(karma=self.karma))

my_life = LifeSimulator()
my_life.life()

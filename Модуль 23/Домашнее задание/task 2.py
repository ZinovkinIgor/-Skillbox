"""
Задача 2. Координаты
Что нужно сделать

Есть файл coordinates.txt, в котором хранится N пар из чисел X и Y. Оба числа передаются в первую функцию,
где к каждой координате прибавляется случайное число (от 0 до 5 и от 0 до 10) и возвращается результат деления X на Y.
Затем эти же координаты передаются во вторую функцию, где уже отнимается случайное число и возвращается Y поделить на X.
После этого формируется случайное число от 0 до 100, и затем в файл result.txt в каждую строку записывается
отсортированный список, состоящий из этого случайного числа и двух полученных результатов.
Один программист уже написал за нас программу для этой задачи, но «почему-то» его вариант решения отклонили. Вот его код:
import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    file = open('coordinates.txt', 'r')
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                file_2 = open('result.txt', 'w')
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(my_list))
            except Exception:
                print("Что-то пошло не так : ")
        except Exception:
            print("Что-то пошло не так со второй функцией")
        finally:
            file.close()
            file_2.close()
except Exception:
    print("Что-то пошло не так с первой функцией")

Отредактируйте и исправьте программу, убрав лишние вложенности try except.

"""

import random


def random_addition(x, y, scor):
    '''
    рандомно добавляем значение к (x,y) далее делим x / y
    добавляем проверку на деление на 0
    добавояем проверку на неверное значение
    '''
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print('Функция 1. Строка {} делить на 0 запрещено.'.format(scor))
        return 0
    except ValueError:
        print('Функция 1. Строка {}, указано неверное значение.'.format(scor))
        return 0



def random_subtraction(x, y, scor):
    '''
    рандомно вычитаем значение от (x,y) далее делим у / х
    добавляем проверку на деление на 0
    добавояем проверку на неверное значение
    '''
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError:
        print('Функция 2. Строка {} делить на 0 запрещено.'.format(scor))
        return 0
    except ValueError:
        print('Функция 2. Строка {}, указано неверное значение.'.format(scor))
        return 0

scor = 0
try:
    with open('coordinates.txt', 'r') as coordinates:
        '''
        Открываем 2 файла, 1 - для чтения и 2 - для записи
        делим строку по значениям, далее запускаем 2 функции на рандомное сложение и вычитание
        далее рандомно добавляем число. Все значие сортирум и вносим в result, 
        ошибки выводим на экран 
        '''
        with open('result.txt', 'a', encoding='utf-8') as result:
            for line in coordinates:
                try:
                    scor += 1
                    meaning = line.split()
                    numbers_addition = random_addition(int(meaning[0]), int(meaning[1]), scor)
                    numbers_subtraction = random_subtraction(int(meaning[0]), int(meaning[1]), scor)
                    random_number = random.randint(0, 100)
                    sorted_value = sorted([numbers_addition, numbers_subtraction, random_number])
                    result.write(' '.join(str(sorted_value)))
                    result.write('\n')
                except ValueError:
                    result.write('Ошибка\n')
                    print('Строка {}, указано неверное значение.'.format(scor))
                except IndexError:
                    result.write('Ошибка\n')
                    print('Строка {},  введено неверное количество данных.'.format(scor))
finally:
    print('Программа завершает работу')
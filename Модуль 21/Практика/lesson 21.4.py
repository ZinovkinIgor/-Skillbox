"""
Задача 1. Ошибка
В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что старший разработчик быстро её нашёл и исправил.
Он решил проверить, смогли бы вы её исправить, если бы его не было на месте. Поэтому он написал для вас код с аналогичной ошибкой:
import random

def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)

nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)

Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее объявленным переменным.
Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям случайное число, в зависимости
от типа данных. Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку и убедитесь, что nums_list,
some_dict и uniq_nums не меняются.

Задача 2. Непонятно!
Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id. Видя, как он мучается,
вы решили помочь ему и объяснить эту тему наглядно.

Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных, информацию о его
изменяемости, а также id этого объекта.

Пример 1:
Введите данные: привет

Тип данных: str (строка)
Неизменяемый (immutable)
Id объекта: 1705156583984

Пример 2:
Введите данные: {‘a’: 10, ‘b’: 20}

Тип данных: dict (словарь)
Изменяемый (mutable)
Id объекта: 1705205308536
"""
task = int(input('Выберите какую задачу выполнить (1, 2, 3): '))

if task == 1:
    # Задача 1
    print('=' * 40)
    import random


    def change_dict(dct):
        num = random.randint(1, 100)
        for i_key, i_value in dct.items():
            if isinstance(i_value, list):
                i_value.append(num)
            if isinstance(i_value, dict):
                i_value[num] = i_key
            if isinstance(i_value, set):
                i_value.add(num)


    nums_list = [1, 2, 3]
    some_dict = {1: 'text', 2: 'another text'}
    uniq_nums = {1, 2, 3}
    common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}

    change_dict(common_dict)
    print(common_dict)

    print('\n\n{}\n{}\n{}\n{}'.format(
        nums_list,
        some_dict,
        uniq_nums,
        common_dict
    ))


elif task == 2:
    # Задача 2
    print('=' * 40)
    print('Задача 2')

    def func(res):
        print('Тип данных: {}'.format(type(res)))
        if type(res) == dict or list or set:
            print('Изменяемый')
        else:
            print('Неизменяемый')
        print(id(res))


    a = 'Привет!'
    b = [1, 2, 3, 4, 5]
    c = {'a': 99, 'r': 88, 'l': 77}
    d = (1, 5, 9.8, 'soup', 44, 3)
    f = (3, 6, 9, 66)
    e = 3
    g = 9.55
    h = True

    while True:
        answer = input('Введите файл: ')
        if answer == 'end':
            break
        elif answer == 'a':
            func(a)
        elif answer == 'b':
            func(b)
        elif answer == 'c':
            func(c)
        elif answer == 'd':
            func(d)
        elif answer == 'f':
            func(f)
        elif answer == 'e':
            func(e)
        elif answer == 'h':
            func(h)
        elif answer == 'g':
            func(g)


elif task == 3:
    # Задача 3
    print('=' * 40)
    print('Задача 3')

else:
    print('Выберите задачу заново.')




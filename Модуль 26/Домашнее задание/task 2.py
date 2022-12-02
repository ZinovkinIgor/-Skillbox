"""
Задача 2. Рефакторинг
Что нужно сделать

После различных вопросов про различия итераторов, генераторов и генераторных выражений на собеседовании вам дали
небольшой пример кода и попросили «провести рефакторинг». Вот сам код:

# Нужно найти, какие два числа из списков в результате попарного перемножения дадут число 56.

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break
Проблема кода состоит в некрасивом выходе из циклов (два break и флаг). Реализуйте более красивый выход из циклов,
используя генератор. Сам алгоритм решения (попарное перемножение) и списки трогать нельзя.
"""

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
def generator(to_find = 56):
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result, )
            if result == to_find:
                yield 'Found!!!'
gen = generator()
for n in gen:
    print(n)



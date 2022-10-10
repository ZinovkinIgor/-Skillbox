"""
Задача 8. Бегущие цифры
Что нужно сделать
Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа. Например,
как в метро, автобусах или трамваях.
Даны список из N элементов и целое число K. Напишите программу, которая циклически сдвигает элементы списка
вправо на K позиций. Используйте минимально возможное количество операций присваивания.

Пример 1:
Сдвиг: 1
Изначальный список: [1, 2, 3, 4, 5]
Сдвинутый список: [5, 1, 2, 3, 4]

Пример 2:
Сдвиг: 3
Изначальный список: [1, 4, -3, 0, 10]
Сдвинутый список: [-3, 0, 10, 1, 4]
"""

def func_shift():
    end_numb = numb_list[-1]
    new_numb_list = []
    new_numb_list.append(end_numb)
    for index in range(len(numb_list) - 1):
        new_numb_list.append(numb_list[index])
    return new_numb_list



shift = int(input('Сдвиг: '))
numb_list = []

for _ in range(5):
    numb = int(input('Введите число: '))
    numb_list.append(numb)
print('Изначальный список:', numb_list)
for _ in range(shift):
    result = func_shift()
    numb_list = result

print('Сдвинутый список:', numb_list)


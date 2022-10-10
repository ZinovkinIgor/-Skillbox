"""
Задача 10. Сортировка
Что нужно сделать

Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран.
Дополнительный список нельзя использовать.
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

Пример:
Изначальный список: [1, 4, -3, 0, 10]
Отсортированный список: [-3, 0, 1, 4, 10]
"""

def sorted_func():
    for row in range(len(number_list)):
        for col in range(len(number_list)):
            if number_list[row] < number_list[col]:
                number_list[row], number_list[col] = number_list[col], number_list[row]


count = int(input('Введите количество цифр в списке: '))
number_list, sorted_number_list = [], []
for _ in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)
print(number_list)
sorted_func()
print(number_list)
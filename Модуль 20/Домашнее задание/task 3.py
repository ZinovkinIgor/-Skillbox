"""
Задача 3. Функция
Что нужно сделать

Напишите функцию, которая на вход принимает кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся
вторым его появлением включительно.
Если элемента нет вовсе — вернуть пустой кортеж.
Если элемент встречается только один раз — вернуть кортеж, который начинается с этого элемента и идёт до конца исходного.
Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Пример вызова функции:
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)
"""

def slicer(numb, n):
    list_n = [i[0] for i in enumerate(numb) if i[1] == n]
    if len(list_n) > 1:
        return numb[list_n[0]:int(list_n[1]) + 1]
    elif len(list_n) == 1:
        return numb[list_n[0]::]
    else:
        return ()

scor = int(input('Введите число: '))
result = slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), scor)
print('Ответ в консоли:', result)





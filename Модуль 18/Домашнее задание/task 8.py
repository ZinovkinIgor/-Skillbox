"""
Задача 8. Бегущая строка
Что нужно сделать
В одном из домашних заданий вы писали для табло программу, которая циклически сдвигает элементы
списка чисел вправо на K позиций. В этот раз вы работаете с двумя строками. Нужно проверить, не
равна ли на самом деле одна другой. Возможно, одна из них просто немного сдвинута.
Пользователь вводит две строки. Напишите программу, которая определяет, можно ли первую строку получить
из второй циклическим сдвигом.
Опционально: если получить можно, то выведите значение этого сдвига.

Пример 1:
Первая строка: abcd
Вторая строка: cdab
Первая строка получается из второй со сдвигом 2.

Пример 2:
Первая строка: abcd
Вторая строка: cdba
Первую строку нельзя получить из второй с помощью циклического сдвига.
"""


line_1 = input('Первая строка: ')
line_2 = input('Вторая строка: ')
new_line = 0
scor = 0
for _ in range(len(line_1)):
    line_1 = ''.join([line_1[len(line_1) - 1], line_1[:len(line_1) - 1]])
    scor += 1
    if line_1 == line_2:
        print('Первая строка получается из второй со сдвигом', scor)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')




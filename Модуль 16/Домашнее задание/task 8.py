"""
Задача 8. Считалка
Что нужно сделать
N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание,
где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N —
это номер человека, который останется в кругу последним.

Пример:
Кол-во человек: 5
Какое число в считалке? 7
Значит, выбывает каждый 7-й человек

Текущий круг людей: [1, 2, 3, 4, 5]
Начало счёта с номера 1
Выбывает человек под номером 2

Текущий круг людей: [1, 3, 4, 5]
Начало счёта с номера 3
Выбывает человек под номером 5

Текущий круг людей: [1, 3, 4]
Начало счёта с номера 1
Выбывает человек под номером 1

Текущий круг людей: [3, 4]
Начало счёта с номера 3
Выбывает человек под номером 3

Остался человек под номером 4
"""

end_scor = 0
human = int(input('Кол-во человек: '))
human_list = list(range(1, human + 1))
number_games = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', str(number_games) + '-й человек')
while len(human_list) > 1:
    print('Текущий круг людей:', human_list)
    print('Начало счёта с номера', human_list[end_scor])
    result = (end_scor + number_games - 1) % len(human_list)
    print('Выбывает человек под номером', human_list[result] - 1)
    human_list.remove(human_list[result])
    end_scor = result % len(human_list)
print('Остался человек под номером', human_list[0])


